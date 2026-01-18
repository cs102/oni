class CreateWords < ActiveRecord::Migration[8.1]
  def change
    create_table :words do |t|
      #t.primary_key :word_id
      t.string :grade
      t.string :prefix
      t.string :suffix
      t.string :definition
      t.string :example
      t.string :origin
      t.string :note

      t.timestamps
    end
  end
end
