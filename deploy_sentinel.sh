#!/bin/bash
# ===========================================================
# PROJECT: BLAZE NOTIFICATION SYSTEM - SECURITY DEPLOY
# ===========================================================
echo "Iniciando despliegue de seguridad..."

# A. Ejecución del Motor
echo "[+] Ejecutando motor de deteccion..."
python3 aml_engine.py

# B. Blindaje de Evidencia (Hardening)
if [ -d "reports/ros_reports" ]; then
    echo "[+] Protegiendo integridad de los reportes..."
    chmod 400 reports/ros_reports/*.json
    echo "========================================================="
    echo "   SISTEMA PROTEGIDO - LISTO PARA AUDITORIA"
    echo "========================================================="
else
    echo "[!] ERROR: No se generaron reportes para proteger."
fi
