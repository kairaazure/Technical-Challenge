# Azure VM Metadata Query

This project provides code examples to query the metadata of an Azure virtual machine and retrieve specific data keys in JSON format.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

This project aims to demonstrate how to retrieve instance metadata from an Azure virtual machine. It provides code examples using PowerShell.

## Prerequisites

Before running the code, you must have the following:

- Azure Subscription: Access to an Azure subscription with the necessary permissions to query virtual machine metadata.
- PowerShell: Install Azure PowerShell module (`Az`).

To retrieve the metadata using PowerShell, follow these steps:

Step 1: Install and Import Azure PowerShell Module:

Make sure you have the Azure PowerShell module installed. If not, you can install it using the following command in PowerShell:

Install-Module -Name Az -Force
Then, import the Azure PowerShell module:
Import-Module Az


Step 2: Authenticate to Azure:

You'll need to sign in to your Azure account to access your resources. Use the following command to sign in:

Connect-AzAccount
It will prompt you to enter your Azure credentials.

Step 3: Retrieve VM Metadata:

Once you are authenticated, you can use the  PowerShell script to retrieve the metadata:
