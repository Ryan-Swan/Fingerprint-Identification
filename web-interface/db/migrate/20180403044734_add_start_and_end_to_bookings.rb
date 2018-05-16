class AddStartAndEndToBookings < ActiveRecord::Migration[5.1]
  def change
    add_column :bookings, :user_id, :integer
  end
end
