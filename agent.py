#!/usr/bin/env python3
"""
System Monitoring Agent
Comprehensive monitoring of CPU, memory, disk, and network metrics
"""

import psutil
import json
import time
from datetime import datetime
from typing import Dict, List, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SystemMonitor:
    """Comprehensive system monitoring agent"""

    def __init__(self, sample_interval: float = 1.0):
        """
        Initialize the system monitor
        
        Args:
            sample_interval: Time interval between samples in seconds
        """
        self.sample_interval = sample_interval
        self.metrics_history = []

    def get_cpu_metrics(self) -> Dict[str, Any]:
        """
        Collect CPU metrics including usage, frequency, and cores
        
        Returns:
            Dictionary with CPU metrics
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=self.sample_interval)
            cpu_count_logical = psutil.cpu_count(logical=True)
            cpu_count_physical = psutil.cpu_count(logical=False)
            cpu_freq = psutil.cpu_freq()
            
            # Per-core CPU usage
            per_core_usage = psutil.cpu_percent(interval=self.sample_interval, percpu=True)
            
            cpu_metrics = {
                'timestamp': datetime.utcnow().isoformat(),
                'overall_percent': cpu_percent,
                'per_core_percent': per_core_usage,
                'logical_cores': cpu_count_logical,
                'physical_cores': cpu_count_physical,
                'frequency': {
                    'current_mhz': round(cpu_freq.current, 2) if cpu_freq else 0,
                    'min_mhz': round(cpu_freq.min, 2) if cpu_freq else 0,
                    'max_mhz': round(cpu_freq.max, 2) if cpu_freq else 0,
                }
            }
            logger.debug(f"CPU metrics collected: {cpu_metrics['overall_percent']}%")
            return cpu_metrics
        except Exception as e:
            logger.error(f"Error collecting CPU metrics: {e}")
            return {}

    def get_memory_metrics(self) -> Dict[str, Any]:
        """
        Collect memory metrics (RAM and swap)
        
        Returns:
            Dictionary with memory metrics
        """
        try:
            virtual_mem = psutil.virtual_memory()
            swap_mem = psutil.swap_memory()
            
            memory_metrics = {
                'timestamp': datetime.utcnow().isoformat(),
                'virtual_memory': {
                    'total_gb': round(virtual_mem.total / (1024**3), 2),
                    'available_gb': round(virtual_mem.available / (1024**3), 2),
                    'used_gb': round(virtual_mem.used / (1024**3), 2),
                    'percent_used': virtual_mem.percent,
                    'active_gb': round(virtual_mem.active / (1024**3), 2),
                    'inactive_gb': round(virtual_mem.inactive / (1024**3), 2),
                },
                'swap_memory': {
                    'total_gb': round(swap_mem.total / (1024**3), 2),
                    'used_gb': round(swap_mem.used / (1024**3), 2),
                    'free_gb': round(swap_mem.free / (1024**3), 2),
                    'percent_used': swap_mem.percent,
                }
            }
            logger.debug(f"Memory metrics collected: {memory_metrics['virtual_memory']['percent_used']}% used")
            return memory_metrics
        except Exception as e:
            logger.error(f"Error collecting memory metrics: {e}")
            return {}

    def get_disk_metrics(self) -> Dict[str, Any]:
        """
        Collect disk metrics for all mounted partitions
        
        Returns:
            Dictionary with disk metrics
        """
        try:
            disk_metrics = {
                'timestamp': datetime.utcnow().isoformat(),
                'partitions': []
            }
            
            # Get all disk partitions
            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    partition_info = {
                        'device': partition.device,
                        'mountpoint': partition.mountpoint,
                        'fstype': partition.fstype,
                        'total_gb': round(usage.total / (1024**3), 2),
                        'used_gb': round(usage.used / (1024**3), 2),
                        'free_gb': round(usage.free / (1024**3), 2),
                        'percent_used': usage.percent,
                    }
                    disk_metrics['partitions'].append(partition_info)
                except PermissionError:
                    logger.warning(f"Permission denied accessing {partition.mountpoint}")
                    continue
            
            # Get disk I/O statistics
            disk_io = psutil.disk_io_counters()
            if disk_io:
                disk_metrics['io_stats'] = {
                    'read_count': disk_io.read_count,
                    'write_count': disk_io.write_count,
                    'read_bytes_gb': round(disk_io.read_bytes / (1024**3), 2),
                    'write_bytes_gb': round(disk_io.write_bytes / (1024**3), 2),
                    'read_time_ms': disk_io.read_time,
                    'write_time_ms': disk_io.write_time,
                }
            
            logger.debug(f"Disk metrics collected for {len(disk_metrics['partitions'])} partitions")
            return disk_metrics
        except Exception as e:
            logger.error(f"Error collecting disk metrics: {e}")
            return {}

    def get_network_metrics(self) -> Dict[str, Any]:
        """
        Collect network metrics including interface statistics and connections
        
        Returns:
            Dictionary with network metrics
        """
        try:
            network_metrics = {
                'timestamp': datetime.utcnow().isoformat(),
                'interfaces': [],
                'connections_summary': {}
            }
            
            # Get network interface statistics
            net_if_stats = psutil.net_if_stats()
            for interface, stats in net_if_stats.items():
                interface_info = {
                    'name': interface,
                    'is_up': stats.isup,
                    'speed_mbps': stats.speed if stats.speed else 0,
                    'mtu': stats.mtu,
                    'packets_sent': stats.packets_sent,
                    'packets_recv': stats.packets_recv,
                    'errors_in': stats.errin,
                    'errors_out': stats.errout,
                    'drops_in': stats.dropin,
                    'drops_out': stats.dropout,
                }
                network_metrics['interfaces'].append(interface_info)
            
            # Get network I/O statistics
            net_io = psutil.net_io_counters()
            if net_io:
                network_metrics['io_stats'] = {
                    'bytes_sent_gb': round(net_io.bytes_sent / (1024**3), 2),
                    'bytes_recv_gb': round(net_io.bytes_recv / (1024**3), 2),
                    'packets_sent': net_io.packets_sent,
                    'packets_recv': net_io.packets_recv,
                    'errors_in': net_io.errin,
                    'errors_out': net_io.errout,
                    'drops_in': net_io.dropin,
                    'drops_out': net_io.dropout,
                }
            
            # Get connection statistics
            try:
                connections = psutil.net_connections()
                conn_by_status = {}
                for conn in connections:
                    status = conn.status
                    conn_by_status[status] = conn_by_status.get(status, 0) + 1
                network_metrics['connections_summary'] = conn_by_status
            except PermissionError:
                logger.warning("Permission denied accessing connection statistics")
            
            logger.debug(f"Network metrics collected for {len(network_metrics['interfaces'])} interfaces")
            return network_metrics
        except Exception as e:
            logger.error(f"Error collecting network metrics: {e}")
            return {}

    def collect_all_metrics(self) -> Dict[str, Any]:
        """
        Collect all system metrics
        
        Returns:
            Dictionary with all system metrics
        """
        all_metrics = {
            'timestamp': datetime.utcnow().isoformat(),
            'cpu': self.get_cpu_metrics(),
            'memory': self.get_memory_metrics(),
            'disk': self.get_disk_metrics(),
            'network': self.get_network_metrics(),
        }
        
        self.metrics_history.append(all_metrics)
        logger.info("All system metrics collected successfully")
        return all_metrics

    def get_system_summary(self) -> Dict[str, Any]:
        """
        Get a summary of critical system metrics
        
        Returns:
            Dictionary with summary metrics
        """
        metrics = self.collect_all_metrics()
        
        summary = {
            'timestamp': metrics['timestamp'],
            'cpu_usage_percent': metrics['cpu'].get('overall_percent', 0),
            'memory_usage_percent': metrics['memory'].get('virtual_memory', {}).get('percent_used', 0),
            'available_memory_gb': metrics['memory'].get('virtual_memory', {}).get('available_gb', 0),
            'disk_usage_summary': {},
            'network_status': 'active' if metrics['network'].get('interfaces') else 'inactive',
        }
        
        # Add disk usage summary
        for partition in metrics['disk'].get('partitions', []):
            summary['disk_usage_summary'][partition['mountpoint']] = {
                'used_gb': partition['used_gb'],
                'total_gb': partition['total_gb'],
                'percent_used': partition['percent_used'],
            }
        
        return summary

    def export_metrics_json(self, filepath: str = None) -> str:
        """
        Export collected metrics to JSON file
        
        Args:
            filepath: Path to save JSON file (optional)
            
        Returns:
            JSON string of metrics
        """
        try:
            latest_metrics = self.metrics_history[-1] if self.metrics_history else self.collect_all_metrics()
            json_str = json.dumps(latest_metrics, indent=2)
            
            if filepath:
                with open(filepath, 'w') as f:
                    f.write(json_str)
                logger.info(f"Metrics exported to {filepath}")
            
            return json_str
        except Exception as e:
            logger.error(f"Error exporting metrics: {e}")
            return "{}"


def main():
    """Main function for agent execution"""
    monitor = SystemMonitor(sample_interval=1.0)
    
    try:
        logger.info("Starting System Monitoring Agent")
        
        # Collect metrics
        all_metrics = monitor.collect_all_metrics()
        summary = monitor.get_system_summary()
        
        # Display summary
        print("\n" + "="*60)
        print("SYSTEM MONITORING SUMMARY")
        print("="*60)
        print(f"Timestamp: {summary['timestamp']}")
        print(f"CPU Usage: {summary['cpu_usage_percent']}%")
        print(f"Memory Usage: {summary['memory_usage_percent']}%")
        print(f"Available Memory: {summary['available_memory_gb']} GB")
        print(f"Network Status: {summary['network_status']}")
        print("\nDisk Usage by Partition:")
        for mountpoint, usage in summary['disk_usage_summary'].items():
            print(f"  {mountpoint}: {usage['used_gb']} GB / {usage['total_gb']} GB ({usage['percent_used']}%)")
        print("="*60 + "\n")
        
        # Export full metrics
        monitor.export_metrics_json('system_metrics.json')
        logger.info("Agent execution completed successfully")
        
    except KeyboardInterrupt:
        logger.info("Agent interrupted by user")
    except Exception as e:
        logger.error(f"Agent error: {e}")
        raise


if __name__ == "__main__":
    main()
