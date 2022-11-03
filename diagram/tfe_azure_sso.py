from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

from diagrams.azure.network import Subnets, VirtualNetworks, VirtualNetworkGateways

from diagrams.azure.compute import VM,VMLinux
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.azure.storage import BlobStorage
from diagrams.azure.identity import ActiveDirectory



# Variables
title = "VPC with 1 public subnet for the TFE server and 1 private subnet for PostgreSQL instance requirement."
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
    with Cluster("aws"):
        bucket_tfe = BlobStorage("TFE bucket")
        bucket_files = BlobStorage("TFE airgap files")
        with Cluster("vpc"):
            igw_gateway = VirtualNetworkGateways("igw")
    
            with Cluster("Availability Zone: eu-north-1a \n\n  "):
                # Subcluster 
                with Cluster("subnet_public1"):
                     ec2_tfe_server = VMLinux("TFE_server")
                   # Subcluster
                with Cluster("subnet_private1"):
                    with Cluster("DB subnet"):
                        postgresql = DatabaseForPostgresqlServers("RDS Instance")

    # Diagram

    user >> bucket_files 

    bucket_tfe
        
    user >> ec2_tfe_server
     
    ec2_tfe_server >> [postgresql,
                       bucket_tfe, 
                       bucket_files]

diag
