class AddFieldsToBookings < ActiveRecord::Migration[5.1]
  def change
    add_column :bookings, :permissions, :string
    add_column :bookings, :user_group_id, :integer
  end
end
