function Get-AzureVMMetadata {
    param (
        [string]$ResourceGroupName,
        [string]$VMName,
        [string]$DataKey
    )

    $vm = Get-AzVM -ResourceGroupName $ResourceGroupName -Name $VMName -Status
    if ($vm) {
        $metadata = @{
            $DataKey = $vm.Tags[$DataKey]
        }
        $metadata | ConvertTo-Json
    }
    else {
        Write-Output "VM not found."
    }
}

# Example usage
$ResourceGroupName = "your-resource-group"
$VMName = "your-vm-name"
$DataKey = "Name"

$jsonOutput = Get-AzureVMMetadata -ResourceGroupName $ResourceGroupName -VMName $VMName -DataKey $DataKey
Write-Output $jsonOutput
