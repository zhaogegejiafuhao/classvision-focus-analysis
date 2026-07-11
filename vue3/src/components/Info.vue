<template>
    <div class="component-5579_152925">
        <div id="5579_152925" class="Pixso-symbol-5579_152925">
            <div
                id="5579_152926"
                class="Pixso-symbol-5579_152926"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_152927">
                    <div
                        id="5579_152927"
                        class="Pixso-vector-5579_152927"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152932"
                class="Pixso-symbol-5579_152932"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_152933">
                    <div
                        id="5579_152933"
                        class="Pixso-vector-5579_152933"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152934"
                class="Pixso-symbol-5579_152934"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_152935">
                    <div
                        id="5579_152935"
                        class="Pixso-vector-5579_152935"
                    ></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Format: { type: String },
    Weight: { type: String }
});
</script>
<style>
.Pixso-symbol-5579_152925 {
}
.Pixso-symbol-5579_152926 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152927 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector62.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5579_152932 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152933 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector60.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5579_152934 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152935 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector61.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
