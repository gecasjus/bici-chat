# class Message(Base):
#     id = Column(String, primary_key=True, default=str(uuid.uuid4()))
#     sender_id = Column(String, nullable=False)
#     chat_id = Column(String, ForeignKey('chat.id', ondelete="CASCADE"), nullable=False)
#     content = Column(String,  nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))