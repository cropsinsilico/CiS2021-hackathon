.. _interface_mapping_table_rst:

| Language | Import                                                             | Input                                            | Output                                            |
|----------|--------------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| R        | ``library(yggdrasil)``                                             | ``YggInterface('YggInput', '{channel_name}')``   | ``YggInterface('YggOutput', '{channel_name}')``   |
| c        | ``#include "YggInterface.h"``                                      | ``yggInputType("{channel_name}", {datatype})``   | ``yggOutputType("{channel_name}", {datatype})``   |
| c++      | ``#include "YggInterface.hpp"``                                    | ``YggInput {channel_obj}("{channel_name}")``     | ``YggOutput {channel_obj}("{channel_name}")``     |
| fortran  | ``use fygg``                                                       | ``ygg_input_type("{channel_name}", {datatype})`` | ``ygg_output_type("{channel_name}", {datatype})`` |
| matlab   |                                                                    | ``YggInterface('YggInput', '{channel_name}')``   | ``YggInterface('YggOutput', '{channel_name}')``   |
| python   | ``from yggdrasil.languages.Python.YggInterface import {commtype}`` | ``YggInput("{channel_name}")``                   | ``YggOutput("{channel_name}")``                   |


| Language | Send                                                        | Recv                                                       |
|----------|-------------------------------------------------------------|------------------------------------------------------------|
| R        | ``flag = {channel_obj}$send({outputs})``                    | ``c(flag, {inputs}) %<-% {channel_obj}$recv()``            |
| c        | ``flag = yggSend({channel_obj}, {outputs})``                | ``flag = yggRecv({channel_obj}, {input_refs})``            |
| c++      | ``flag = {channel_obj}.send({nargs}, {outputs})``           | ``flag = {channel_obj}.recv({nargs}, {input_refs})``       |
| fortran  | ``flag = ygg_send_var({channel_obj}, [yggarg({outputs})])`` | ``flag = ygg_recv_var({channel_obj}, [yggarg({inputs})])`` |
| matlab   | ``flag = {channel_obj}.send({outputs})``                    | ``[flag, {inputs}] = {channel_obj}.recv()``                |
| python   | ``flag = {channel_obj}.send({outputs})``                    | ``flag, {inputs} = {channel_obj}.recv()``                  |


| Language | Server                                                                          | Client                                                                          | Call                                                                            |
|----------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| R        | ``YggInterface('YggRpcServer', '{channel_name}')``                              | ``YggInterface('YggRpcClient', '{channel_name}')``                              | ``c(flag, {inputs}) %<-% {channel_obj}$call({outputs})``                        |
| c        | ``yggRpcServerType("{channel_name}", {datatype_in}, {datatype_out})``           | ``yggRpcClientType("{channel_name}", {datatype_out}, {datatype_in})``           | ``flag = rpcCall({channel_obj}, {outputs}, {inputs})``                          |
| c++      | ``YggRpcServer {channel_obj}("{channel_name}", {datatype_in}, {datatype_out})`` | ``YggRpcClient {channel_obj}("{channel_name}", {datatype_out}, {datatype_in})`` | ``flag = {channel_obj}.call({nargs}, {outputs}, {input_refs})``                 |
| fortran  | ``ygg_rpc_server_type("{channel_name}", {datatype_in}, {datatype_out})``        | ``ygg_rpc_client_type("{channel_name}", {datatype_out}, {datatype_in})``        | ``flag = ygg_rpc_call({channel_obj}, [yggarg({outputs})], [yggarg({inputs})])`` |
| matlab   | ``YggInterface('YggRpcServer', '{channel_name}')``                              | ``YggInterface('YggRpcClient', '{channel_name}')``                              | ``[flag, {inputs}] = {channel_obj}.call({outputs})``                            |
| python   | ``YggRpcServer("{channel_name}")``                                              | ``YggRpcClient("{channel_name}")``                                              | ``flag, {inputs} = {channel_obj}.call({outputs})``                              |


| Language | Timesync                                                        |
|----------|-----------------------------------------------------------------|
| R        | ``YggInterface('YggTimesync', '{channel_name}')``               |
| c        | ``yggTimesync("{channel_name}", "{time_units}")``               |
| c++      | ``YggTimesync {channel_obj}("{channel_name}", "{time_units}")`` |
| fortran  | ``yggTimesync("{channel_name}", "{time_units}")``               |
| matlab   | ``YggInterface('YggTimesync', '{channel_name}')``               |
| python   | ``YggTimesync("{channel_name}")``                               |

