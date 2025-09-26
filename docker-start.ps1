# PowerShell script to start MCP service Docker container
# This script runs the container in detached mode with automatic cleanup

Write-Host "Starting MCP Service Docker container..." -ForegroundColor Green

# Run the Docker container
docker run --rm -d -p 8080:8000 mcp-service

# Check if the command was successful
if ($LASTEXITCODE -eq 0) {
    Write-Host "MCP Service container started successfully!" -ForegroundColor Green
    Write-Host "Container is running on http://localhost:8080" -ForegroundColor Cyan
    Write-Host "MCP endpoint available at: http://localhost:8080/mcp" -ForegroundColor Cyan

    # Show running containers
    Write-Host "`nRunning containers:" -ForegroundColor Yellow
    docker ps --filter "ancestor=mcp-service" --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
} else {
    Write-Host "Failed to start MCP Service container!" -ForegroundColor Red
    Write-Host "Please check if the Docker image 'mcp-service' exists and Docker is running." -ForegroundColor Yellow
}