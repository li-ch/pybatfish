# coding=utf-8
#   Copyright 2018 The Batfish Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


class Flow(object):
    # "dscp" : 0,
    # "dstIp" : "2.128.0.101",
    # "dstPort" : 22,
    # "ecn" : 0,
    # "fragmentOffset" : 0,
    # "icmpCode" : 255,
    # "icmpVar" : 255,
    # "ingressInterface" : "Ethernet1/0",
    # "ingressNode" : "as2core1",
    # "ingressVrf" : "default",
    # "ipProtocol" : "TCP",
    # "packetLength" : 0,
    # "srcIp" : "253.127.0.0",
    # "srcPort" : 0,
    # "state" : "NEW",
    # "tag" : "DIFFERENTIAL",
    # "tcpFlagsAck" : 0,
    # "tcpFlagsCwr" : 0,
    # "tcpFlagsEce" : 0,
    # "tcpFlagsFin" : 0,
    # "tcpFlagsPsh" : 0,
    # "tcpFlagsRst" : 0,
    # "tcpFlagsSyn" : 0,
    # "tcpFlagsUrg" : 0

    def __init__(self, jsonObject):
        self.__dict__ = jsonObject

    def __str__(self):
        # exclude the tag field
        iface_str = "ingressInterface: {}".format(
            self.ingressInterface) if hasattr(self, "ingressInterface") else ""
        vrf_str = "vrf: {}".format(self.ingressVrf) if hasattr(self,
                                                               "ingressVrf") and self.ingressVrf != "default" else ""
        return \
            "{node}{iface}{vrf}->[{src_ip}:{src_port}->{dst_ip}:{dst_port}" \
            " proto: {proto} dscp:{dscp} ecn:{ecn} fragOff:{offset} length" \
            ":{length} state:{state} flags: {flags}".format(
                node=self.ingressNode,
                iface=iface_str,
                vrf=vrf_str,
                src_ip=self.srcIp,
                src_port=self.srcPort,
                dst_ip=self.dstIp,
                dst_port=self.dstPort,
                proto=self.ipProtocol,
                dscp=self.dscp,
                ecn=self.ecn,
                offset=self.fragmentOffset,
                length=self.packetLength,
                state=self.state,
                flags=self.get_flag_str())

    def get_flag_str(self):
        if self.ipProtocol == 6:
            "{}{}{}{}{}{}{}{}".format(self.tcpFlagsAck, self.tcpFlagsCwr,
                                      self.tcpFlagsEce, self.tcpFlagsFin,
                                      self.tcpFlagsPsh, self.tcpFlagsRst,
                                      self.tcpFlagsSyn, self.tcpFlagsUrg)
        else:
            return "n/a"
