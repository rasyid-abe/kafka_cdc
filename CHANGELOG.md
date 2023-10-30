# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.11.1] - 2023-08-01
- feature/product_bundle [abdur.rasyid@majoo.id]
### Changed
- config
    - cdc
        - prod
            - source_klopos.json
            ``add table include list - m_item_attribute``
            - sink_m_item_attribute.json
            ``change topics name``
        - staging
            - source_klopos.json
            ``add table include list - m_item_attribute``
            - sink_m_item_attribute.json
            ``change topics name``
### Removed
- config
    - cdc
        - prod
            - source_klopos_m_item_attribute.json
        - staging
            - source_klopos_m_item_attribute.json

## [1.11.0] - 2023-07-27
- feature/product_bundle [abdur.rasyid@majoo.id]
- Ahmad-Irsyadur-Roziqin/jenkinsfile-edited-online-with-bitbucket-1690799051208 [ahmad.roziqin@majoo.id]
### Added
- configs
    - cdc
        - prod
            - source_klopos_m_item_attribute.json
            - sink_m_item_attribute.json
        - staging
            - source_klopos_m_item_attribute.json
            - sink_m_item_attribute.json
- Jenkinsfile ``ubah host ip pub ke private, karna jenkin pindah ke gcp``

## [1.10.3] - 2023-07-14
- feature/update-debezium-mongodb [wikan.kuncara@majoo.id]
- update-infra [ahmad.roziqin@majoo.id]
### Changed
- configs
    - cdc
        - prod
            - sink_m_item_postgres.json
            - sink_reference_order_type_category.json
            - source_inventory_majoolite.json
            - source_inventory.json
            - source_klopos.json
            - source_payroll.json
            - source_user_management.json
            ``fix: change connector names and mongodb configs after version update``
- infrastructure
    - kafka
        - kafka-connect-prod.yaml
        - kafkaui-prod.yaml
        ``update compose``

## [1.10.2] - 2023-07-13
- Ahmad-Irsyadur-Roziqin/jenkinsfile-edited-online-with-bitbucket-1689246128527 [ahmad.roziqin@majoo.id]
### Changed
- Jenkinsfile
``edit config migrasi VM to GCP``

## [1.10.1] - 2023-07-05
- fix/binlog-expired-prod [wikan.kuncara@majoo.id]
- Ahmad-Irsyadur-Roziqin/jenkinsfile-edited-online-with-bitbucket-1689096172544 [ahmad.roziqin@majoo.id]
### Changed
- Jenkinsfile
``migrasi VM``
### Removed
- configs
    - cdc
        - prod
            - sink_user_management_master_data.json
        - staging
            - sink_user_management_master_data.json

## [1.10.0] - 2023-07-05
- feature/cdc-produk-majoolite [vera@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_inventory_majoolite_category_postgres.json
            - sink_inventory_majoolite_inventory_history_postgres.json
            - sink_inventory_majoolite_item_postgres.json
            - sink_inventory_majoolite_periodic_balance_postgres.json
            - source_inventory_majoolite.json
        -staging
            - sink_inventory_majoolite_category_postgres.json
            - sink_inventory_majoolite_inventory_history_postgres.json
            - sink_inventory_majoolite_item_postgres.json
            - sink_inventory_majoolite_periodic_balance_postgres.json
            - source_inventory_majoolite.json

## [1.9.1] - 2023-06-22
- feature/cdc-user-management [m.miftakhul@majoo.id]
### Changed
- configs
    - cdc
        - prod
            - sink_user_management_master_data.json
            ``Rename topic``
            - sink_user_management_merchant.json
            ``Rename topic``
            - sink_user_management_outlet.json
            ``Rename topic``
            - sink_user_management_subscription_lite.json
            ``Rename topic``
            - sink_user_management_user.json
            ``Rename topic``
            - source_user_management.json
            ``Change mongodb name``

## [1.9.0] - 2023-06-15
- feature/cdc-mongodb-postgres [abdur.rasyid@majoo.id]
- feature/cdc-transaction-majoolite [vera@majoo.id]
- feature/cdc-transaction-majoolite-prod [vera@majoo.id]
- feature/cdc-user-management [m.miftakhul@majoo.id]
- feature/cdc-reference-order-type [muhammad.muzakki@majoo.id]
- feature/cdc-serialnumber-tracking [muhammad.muzakki@majoo.id]
- feature/stock_in [muhammad.muzakki@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_freemium_order_cash_postgres.json
            - sink_freemium_order_customer_address_postgres.json
            - sink_freemium_order_customer_cart_postgres.json
            - sink_freemium_order_customer_group_postgres.json
            - sink_freemium_order_customer_postgres.json
            - sink_freemium_order_delivery_order_detail_postgres.json
            - sink_freemium_order_delivery_order_postgres.json
            - sink_freemium_order_invoice_payment_postgres.json
            - sink_freemium_order_invoice_postgres.json
            - sink_freemium_order_m_payment_postgres.json
            - sink_freemium_order_m_tax_detail_postgres.json
            - sink_freemium_order_m_tax_postgres.json
            - sink_freemium_order_payment_method_detail_postgres.json
            - sink_freemium_order_payment_method_setting_detail_postgres.json
            - sink_freemium_order_payment_method_setting_postgres.json
            - sink_freemium_order_payment_postgres.json
            - sink_freemium_order_petty_cash_postgres.json
            - sink_freemium_order_receipt_setting_outlet_postgres.json
            - sink_freemium_order_receipt_setting_postgres.json
            - sink_freemium_order_reference_order_type_postgres.json
            - sink_freemium_order_reference_status_postgres.json
            - sink_freemium_order_sales_delivery_info_postgres.json
            - sink_freemium_order_sales_invoice_postgres.json
            - sink_freemium_order_sales_postgres.json
            - sink_freemium_order_sales_product_postgres.json
            - sink_freemium_order_sales_promo_postgres.json
            - sink_freemium_order_sales_type_postgres.json
            - sink_freemium_order_tax_setting_postgres.json
            - sink_inventory_batchnumber_tracking_postgres.json
            - sink_inventory_serialnumber_tracking_postgres.json
            - sink_inventory_stock_in_postgres.json
            - sink_reference_order_type_category.json
            - sink_user_management_master_data.json
            - sink_user_management_merchant.json
            - sink_user_management_outlet.json
            - sink_user_management_subscription_lite.json
            - sink_user_management_user.json
            - source_freemium_order.json
        - staging
            - sink_freemium_order_cash_postgres.json
            - sink_freemium_order_customer_address_postgres.json
            - sink_freemium_order_customer_cart.json
            - sink_freemium_order_customer_group_postgres.json
            - sink_freemium_order_customer_postgres.json
            - sink_freemium_order_delivery_order_detail_postgres.json
            - sink_freemium_order_delivery_order_postgres.json
            - sink_freemium_order_invoice_payment_postgres.json
            - sink_freemium_order_invoice_postgres.json
            - sink_freemium_order_m_payment_postgres.json
            - sink_freemium_order_m_tax_detail_postgres.json
            - sink_freemium_order_m_tax_postgres.json
            - sink_freemium_order_payment_method_detail_postgres.json
            - sink_freemium_order_payment_method_setting_detail_postgres.json
            - sink_freemium_order_payment_method_setting_postgres.json
            - sink_freemium_order_payment_postgres.json
            - sink_freemium_order_petty_cash_postgres.json
            - sink_freemium_order_receipt_setting_outlet_postgres.json
            - sink_freemium_order_receipt_setting_postgres.json
            - sink_freemium_order_reference_order_type_postgres.json
            - sink_freemium_order_reference_status_postgres.json
            - sink_freemium_order_sales_delivery_info_postgres.json
            - sink_freemium_order_sales_invoice_postgres.json
            - sink_freemium_order_sales_postgres.json
            - sink_freemium_order_sales_product_postgres.json
            - sink_freemium_order_sales_promo_postgres.json
            - sink_freemium_order_sales_type_postgres.json
            - sink_freemium_order_tax_setting_postgres.json
            - sink_inventory_batchnumber_tracking_postgres.json
            - sink_inventory_serialnumber_tracking_postgres.json
            - sink_inventory_stock_in_postgres.json
            - sink_reference_order_type_category.json
            - sink_user_management_master_data.json
            - sink_user_management_merchant.json
            - sink_user_management_outlet.json
            - sink_user_management_subscription_lite.json
            - sink_user_management_user.json
            - source_freemium_order.json
### Changed
- configs
    - cdc
        - prod
            - source_payroll.json
            ``change hosts and set mongodb.members.auto.discover true``
            - sink_payroll_shift_reporting.json
            ``change topic``
            - sink_m_user_has_support_active_postgres.json
            ``add RenameKey transforms``
            - source_inventory.json
            ``add tb inventory_serialnumber_tracking, inventory_batchnumber_tracking & stock_in``
            - source_klopos.json
            ``add tb reference_order_type_category``
        - staging
            - source_payroll.json
            ``change hosts and set mongodb.members.auto.discover true``
            - sink_payroll_shift_reporting.json
            ``change topic``
            - sink_m_user_has_support_active_postgres.json
            ``add RenameKey transforms``
            - sink_reference_order_type_category.json
            ``change config task mask from 20 to 30``
            - source_inventory.json
            ``add tb inventory_serialnumber_tracking, inventory_batchnumber_tracking & stock_in``
            - source_klopos.json
            ``add tb reference_order_type_category``

## [1.8.1] - 2023-05-31
- feature/cdc-stock-opname [muhammad.muzakki@majoo.id]
### Changed
- configs
    - cdc
        - prod
            - sink_stock_masuk_postgres.json
            ``added column transformation for 'updatedate'``
            - sink_stock_opname_postgres.json
            ``added column transformation for 'updatedate'``

## [1.8.0] - 2023-05-25
- feature/cdc-mongodb-postgres [abdru.rasyid@majoo.id]
- feature/cdc-stock-opname [muhammad.muzakki@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_stock_opname_postgres.json
        - staging
            - sink_stock_opname_postgres.json
### Changed
- configs
    - cdc
        - prod
            - sink_m_item_postgres.json
            ``change config tasks.max from 1 to 20 for multi consumer``
            - source_klopos.json
            ``add table Stock_Opname``
            - sink_payroll_shift_reporting.json
            ``change name topic & name connetor``
            - source_payroll.json
            ``change name connector & db, change value hosts``
        - staging
            - source_klopos_v2.json
            ``add table Stock_Opname``
            - source_klopos.json
            ``add table Stock_Opname``
### Fixed
- configs
    - cdc
        - prod
            - sink_stock_masuk_postgres.json
            ``fixing name table``

## [1.7.0] - 2023-05-04
- feature/cdc-mongodb-postgres [abdru.rasyid@majoo.id]
- feature/cdc-iap-multiconsumer [muhammad.muzakki@majoo.id]
- feature/cdc-stock-masuk [muhammad.muzakki@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_payroll_shift_reporting.json
            - source_payroll.json
            - sink_stock_masuk_postgres.json
        - staging
            - sink_payroll_shift_reporting.json
            - source_payroll.json
            - sink_stock_masuk_postgres.json
### Changed
- configs
    - cdc
        - prod
            - sink_Item_Average_Prices_postgres.json
            ``change config tasks.max from 1 to 20 for multi consumer``
            - source_klopos.json
            ``add table Stock_Masuk``
        - staging
            - source_klopos_v2.json
            - source_klopos.json
            ``add table Stock_Masuk``

## [1.6.0] - 2023-04-11
- feature/coupon-configs [akbar.noto@majoo.id]
- fix/iap_summary [muhammad.muzakki@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_voucher_postgres.json
            - source_klopos2.json
### Changed
- configs
    - cdc
        - prod
            - sink_Item_Average_Prices_postgres.json
            ``handle field transaction_date``
        - staging
            - sink_voucher_postgres.json
            ``handle if value date 0000-00-00 and change topic``
            - sink_iap_summary_by_date_postgres.json
            ``change topics value``
            - sink_Item_Average_Prices_postgres.json
            ``handle field transaction_date``

## [1.5.1] - 2023-03-02
- feature/m-user-has-m-cabang [wikan.kuncara@majoo.id]
### Added
- configs
    - cdc
        - prod
            - sink_m_user_has_m_cabang.json
        - staging
            - sink_m_user_has_m_cabang.json
### Changed
- configs
    - cdc
        - prod
            - source_klopos.json
            ``add table m_user_has_m_cabang``
        - staging
            - source_klopos.json
            ``add table m_user_has_m_cabang``

## [1.5.0] - 2023-03-02
- feature/delete-mysql-sink-connector [wikan.kuncara@majoo.id]
### Remove
- configs
    - cdc
        - prod
            - sink_add_ons_detail.json
            - sink_akunting.json
            - sink_departement.json
            - sink_iap_summary_by_date.json
            - sink_item_variant.json
            - sink_jenis_trx.json
            - sink_kategori_akunting.json
            - sink_m_add_ons.json
            - sink_m_cabang.json
            - sink_m_category_item.json
            - sink_m_customer.json
            - sink_m_item_has_m_category_item.json
            - sink_m_item_unit.json
            - sink_m_item.json
            - sink_m_jenis_usaha.json
            - sink_m_kota.json
            - sink_m_negara.json
            - sink_m_provinsi.json
            - sink_m_user_has_support_active.json
            - sink_m_user_has_support.json
            - sink_m_user_recap.json
            - sink_m_user.json
            - sink_payment_method.json
            - sink_pm_account.json
            - sink_referal_voucher_transaction.json
            - sink_reference_status.json
            - sink_reference_stock.json
            - sink_reference_transaction_type.json
            - sink_support.json
        - staging
            - sink_add_ons_detail.json
            - sink_akunting.json
            - sink_departement.json
            - sink_iap_summary_by_date.json
            - sink_item_variant.json
            - sink_jenis_trx.json
            - sink_kategori_akunting.json
            - sink_m_add_ons.json
            - sink_m_cabang.json
            - sink_m_category_item.json
            - sink_m_customer.json
            - sink_m_item_has_m_category_item.json
            - sink_m_item_unit.json
            - sink_m_item.json
            - sink_m_jenis_usaha.json
            - sink_m_kota.json
            - sink_m_negara.json
            - sink_m_provinsi.json
            - sink_m_user_has_support_active.json
            - sink_m_user_has_support.json
            - sink_m_user_recap.json
            - sink_m_user.json
            - sink_payment_method.json
            - sink_pm_account.json
            - sink_referal_voucher_transaction.json
            - sink_reference_status.json
            - sink_reference_stock.json
            - sink_reference_transaction_type.json
            - sink_support.json
