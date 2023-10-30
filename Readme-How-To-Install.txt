# Kafka
## How to install
1. Masuk ke dir /home/majoo/svc-data-cdc/infrastructure/kafka,
   Run docker file using `docker compose -f kafka.yaml up -d` (docker compose tsb ada container kafka-ui, kafka-broker & kafka zookeeper)
2. Run docker compose file untuk kafka connect staging 'docker compose -f kafka-connect-stg.yaml up -d'
3. Jalankan, masuk dulu ke dir svc-data-cdc lalu run '. ./export-env.sh' (pastikan .env available di dir tersebut)
4. Run 'python3 cicd.py --env staging'
5. Check docker status using 'docker ps' (Pastikan container kafka-connect status healthy)
6. Go to browser then browse for [Kafka Dev] address

[Kafka Dev]: http://10.132.0.31:8000/ (Kafka Dev)
[Kafka Prod]: http://10.130.248.69:8000/ (Kafka Prod)

##URL secret conector ke DB
/home/majoo/svc-data-cdc/infrastructure/kafka/kafka-connect/secrets

##Troubleshooting
- Jika ubah dir docker utama error Command [/usr/local/bin/dub path /etc/kafka/ writable] FAILED ! >> coba pastikan setup mounting disk sudah betul (https://cloud.google.com/compute/docs/disks/add-persistent-disk
)
- Jika kafka1 & registry selalu exited saat running compose kafkaui & kafka-connect pastikan registry yang ada di kafka-connect disable lalu jalankan docker compose up masing2 compose
