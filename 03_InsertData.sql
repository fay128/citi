-- insert task data 
INSERT INTO task(task_name) VALUES('CLASSIFICATION');
INSERT INTO task(task_name) VALUES('NER');

-- insert client data  
INSERT INTO client(client_name, status) VALUES('QMA', 'ACTIVE');

-- insert doc_type data  
INSERT INTO doc_type(doc_type_name, client_name) VALUES('EMAIL', 'QMA');
INSERT INTO doc_type(doc_type_name, client_name) VALUES('SWIFT599', 'QMA');

-- insert client_task_doc_type data  
INSERT INTO client_task_doc_type(client_name, task_name, doc_type_name ) VALUES('QMA', 'CLASSIFICATION', 'EMAIL');
INSERT INTO client_task_doc_type(client_name, task_name, doc_type_name ) VALUES('QMA', 'NER', 'EMAIL');
INSERT INTO client_task_doc_type(client_name, task_name, doc_type_name ) VALUES('QMA', 'CLASSIFICATION', 'SWIFT599');
INSERT INTO client_task_doc_type(client_name, task_name, doc_type_name ) VALUES('QMA', 'NER', 'SWIFT599');