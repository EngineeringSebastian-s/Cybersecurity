import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator;

class Mapper {
    ObjectMapper inseguro() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.activateDefaultTyping(BasicPolymorphicTypeValidator.builder().build(), ObjectMapper.DefaultTyping.NON_FINAL);
        return mapper;
    }
}
