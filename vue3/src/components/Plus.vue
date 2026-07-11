<template>
    <div class="component-5579_150992">
        <div id="5579_150992" class="Pixso-symbol-5579_150992">
            <div
                id="5579_150993"
                class="Pixso-symbol-5579_150993"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_150994">
                    <div
                        id="5579_150994"
                        class="Pixso-vector-5579_150994"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_150999"
                class="Pixso-symbol-5579_150999"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151000">
                    <div
                        id="5579_151000"
                        class="Pixso-vector-5579_151000"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151001"
                class="Pixso-symbol-5579_151001"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151002">
                    <div
                        id="5579_151002"
                        class="Pixso-vector-5579_151002"
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
.Pixso-symbol-5579_150992 {
}
.Pixso-symbol-5579_150993 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_150994 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector126.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-symbol-5579_150999 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151000 {
    width: 78.12%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector124.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5579_151001 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151002 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector125.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
