import logging
from concurrent.futures import ThreadPoolExecutor

import grpc
import numpy as np
from datetime import datetime
from pb import outliers_pb2 as pb2
from pb.outliers_pb2_grpc import OutliersServicer, add_OutliersServicer_to_server
from reports.report import ClusterConfig


def find_outliers(data: np.ndarray):
    """Return indices where values more than 2 standard deviations from mean"""
    out = np.where(np.abs(data - data.mean()) > 2 * data.std())
    # np.where returns a tuple for each dimension, we want the 1st element
    return out[0]


def cluster_config_report():
    f = open("test.xlsx", "rb")
    f.seek(0)
    b = f.read()
    return b


def cluster_replica_report():
    f = open("test.xlsx", "rb")
    f.seek(0)
    b = f.read()
    return b


class OutliersServer(OutliersServicer):
    reports = [ClusterConfig, ClusterConfig]

    def Detect(self, request, context):
        logging.info('detect request size: %d', len(request.metrics))
        # Convert metrics to numpy array of values only
        b = 2 + 2
        data = np.fromiter((m.value for m in request.metrics), dtype='float64')
        indices = find_outliers(data)
        logging.info('found %d outliers', len(indices))
        resp = pb2.OutliersResponse(indices=indices)
        return resp

    # get name report and send it
    def Report(self, request, context):
        f = request.param
        # f = request.param.value
        start = datetime.fromtimestamp(request.start)
        end = request.end
        report = self.reports[request.report]().get_report()
        resp = pb2.ReportB(report=report)
        return resp


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    server = grpc.server(ThreadPoolExecutor())
    add_OutliersServicer_to_server(OutliersServer(), server)
    port = 9999
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info('server ready on port %r', port)
    server.wait_for_termination()
