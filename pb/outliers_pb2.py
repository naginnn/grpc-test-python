# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: outliers.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eoutliers.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\"O\n\x06Metric\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01\".\n\x0fOutliersRequest\x12\x1b\n\x07metrics\x18\x01 \x03(\x0b\x32\n.pb.Metric\"#\n\x10OutliersResponse\x12\x0f\n\x07indices\x18\x01 \x03(\x05\"T\n\nReportType\x12\x1b\n\x06report\x18\x01 \x01(\x0e\x32\x0b.pb.Reports\x12\r\n\x05param\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\"\x19\n\x07ReportB\x12\x0e\n\x06report\x18\x01 \x01(\x0c*5\n\x07Reports\x12\x11\n\rClusterConfig\x10\x00\x12\x17\n\x13\x43lusterConfigMetric\x10\x01\x32j\n\x08Outliers\x12\x35\n\x06\x44\x65tect\x12\x13.pb.OutliersRequest\x1a\x14.pb.OutliersResponse\"\x00\x12\'\n\x06Report\x12\x0e.pb.ReportType\x1a\x0b.pb.ReportB\"\x00\x42%Z#github.com/naginnn/GoPythonGrpcTestb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'outliers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#github.com/naginnn/GoPythonGrpcTest'
  _globals['_REPORTS']._serialized_start=334
  _globals['_REPORTS']._serialized_end=387
  _globals['_METRIC']._serialized_start=55
  _globals['_METRIC']._serialized_end=134
  _globals['_OUTLIERSREQUEST']._serialized_start=136
  _globals['_OUTLIERSREQUEST']._serialized_end=182
  _globals['_OUTLIERSRESPONSE']._serialized_start=184
  _globals['_OUTLIERSRESPONSE']._serialized_end=219
  _globals['_REPORTTYPE']._serialized_start=221
  _globals['_REPORTTYPE']._serialized_end=305
  _globals['_REPORTB']._serialized_start=307
  _globals['_REPORTB']._serialized_end=332
  _globals['_OUTLIERS']._serialized_start=389
  _globals['_OUTLIERS']._serialized_end=495
# @@protoc_insertion_point(module_scope)