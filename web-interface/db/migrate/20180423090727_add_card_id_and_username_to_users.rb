class AddCardIdAndUsernameToUsers < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :card_id, :string
    add_column :users, :username, :string
  end
end
