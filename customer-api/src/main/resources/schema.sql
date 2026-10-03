create table customers (
    customer_number varchar(20) primary key,
    name varchar(100) not null,
    resident_id_masked varchar(20) not null
);

create table capital_contracts (
    id bigint primary key,
    customer_number varchar(20) not null,
    principal decimal(19, 2) not null,
    status varchar(20) not null,
    constraint fk_contract_customer foreign key (customer_number) references customers(customer_number)
);
