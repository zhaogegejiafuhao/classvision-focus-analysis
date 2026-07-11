<template>
    <div class="component-5579_153457">
        <div id="5579_153457" class="Pixso-symbol-5579_153457">
            <div
                id="5579_153458"
                class="Pixso-symbol-5579_153458"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_153459">
                    <div
                        id="5579_153459"
                        class="Pixso-vector-5579_153459"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153464"
                class="Pixso-symbol-5579_153464"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_153465">
                    <div
                        id="5579_153465"
                        class="Pixso-vector-5579_153465"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_153466"
                class="Pixso-symbol-5579_153466"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_153467">
                    <div
                        id="5579_153467"
                        class="Pixso-vector-5579_153467"
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
.Pixso-symbol-5579_153457 {
}
.Pixso-symbol-5579_153458 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153459 {
    width: 87.5%;
    height: 75%;
    background-image: url(@/assets/images/Vector92.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 6.25%;
}
.Pixso-symbol-5579_153464 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153465 {
    width: 90.62%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector90.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 4.69%;
}
.Pixso-symbol-5579_153466 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_153467 {
    width: 87.5%;
    height: 75.01%;
    background-image: url(@/assets/images/Vector91.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 6.24%;
}
</style>
