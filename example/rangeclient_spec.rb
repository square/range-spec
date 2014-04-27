require 'rangeclient'

describe 'Range::Client#compress' do
  let(:client) { Range::Client.new }

  BASE_DIR = File.expand_path("../../spec/compress", __FILE__)

  def self.spec_directory(dir)
    describe do
      Dir[dir + '/*.spec'].each do |spec|
        current = {}
        File.read(spec).lines.each_with_index do |line, i|
          next if line.strip.start_with?("#")

          line.chomp!

          if line.empty?
            specify "%s:%i" % [spec.gsub(BASE_DIR + '/', ''), i + 1] do
              expect(client.compress(current[:result])).to eq(current[:expr])
            end
            current = {}
          else
            if current[:expr]
              current[:result] ||= []
              current[:result] << line
            else
              current[:expr] = line
            end
          end
        end
      end

      Dir.entries(dir).each do |dir|
        if File.directory?(dir) && !%w(. ..).include?(dir)
          spec_directory dir
        end
      end
    end
  end

  spec_directory BASE_DIR
end
