function File_exists(file)
	local f = io.open(file, "rb")
	if f then
		f:close()
	end
	return f ~= nil
end

function Lines_from(file)
	if not File_exists(file) then
		return {}
	end
	local lines = {}
	for line in io.lines(file) do
		lines[#lines + 1] = line
	end
	return lines
end

function MySplit(inputstr, sep)
	if sep == nil then
		sep = "%s"
	end
	local t = {}
	for str in string.gmatch(inputstr, "([^" .. sep .. "]+)") do
		table.insert(t, str)
	end
	return t
end

local file = "./day2/input"
local lines = Lines_from(file)
local result = 0

for i = 1, #lines, 1 do
	local line = MySplit(lines[i])
	local previous_number
	for v = 1, #line, 1 do
		if v == 1 then
			previous_number = tonumber(line[v])
		else
			local step = tonumber(line[v]) - previous_number
		end
	end
end

print(result)
