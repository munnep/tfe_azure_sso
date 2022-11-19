from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

from diagrams.azure.network import Subnets, VirtualNetworks, VirtualNetworkGateways

from diagrams.azure.compute import VM,VMLinux
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.azure.storage import BlobStorage
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.network import ApplicationGateway



# Variables
title = "VPC with 2 public subnet for the bastion client and application gateway \ and 2 private subnet for TFE and PostgreSQL instance requirement."
outformat = "png"
filename = "diagram_tfe_azure_sso"
direction = "TB"


with Diagram(
    name=title,
    direction=direction,
    filename=filename,
    outformat=outformat,
) as diag:
    # Non Clustered
    user = Server("user")

    # Cluster 
    with Cluster("Azure"):
        bucket_tfe = BlobStorage("TFE bucket")
        with Cluster("vpc"):
    
            with Cluster("Availability Zone: xxx \n\n  "):
                # Subcluster 
                with Cluster("subnet_public1"):
                    ApplicationGateway = ApplicationGateway("ApplicationGateway")
                with Cluster("subnet_public2"):
                    ec2_bastion = VMLinux("bastion")
                with Cluster("subnet_private1"):
                     ec2_tfe_server = VMLinux("TFE_server")
                with Cluster("subnet_private2"):     
                     postgresql = DatabaseForPostgresqlServers("RDS Instance")

    # Diagram

    user >> ec2_bastion >> ec2_tfe_server

        
    user >> ApplicationGateway >> ec2_tfe_server
     
    ec2_tfe_server >> [postgresql,
                       bucket_tfe]

diag
