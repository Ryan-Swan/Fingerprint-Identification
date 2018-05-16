class CreateAuthenticationLogs < ActiveRecord::Migration[5.1]
  def change
    create_table :authentication_logs do |t|
      t.integer :user_id
      t.boolean :unathorized

      t.timestamps
    end
  end
end
