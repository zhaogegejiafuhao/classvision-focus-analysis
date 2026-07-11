<template>
    <div class="component-5578_149504">
        <div id="5578_149504" class="Pixso-symbol-5578_149504">
            <div
                id="5578_149505"
                class="Pixso-symbol-5578_149505"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149506">
                    <div
                        id="5578_149506"
                        class="Pixso-vector-5578_149506"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149511"
                class="Pixso-symbol-5578_149511"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149512">
                    <div
                        id="5578_149512"
                        class="Pixso-vector-5578_149512"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149513"
                class="Pixso-symbol-5578_149513"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149514">
                    <div
                        id="5578_149514"
                        class="Pixso-vector-5578_149514"
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
.Pixso-symbol-5578_149504 {
}
.Pixso-symbol-5578_149505 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149506 {
    width: 78.13%;
    height: 56.25%;
    background-image: url(@/assets/images/Vector41.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 9.37%;
    top: 25%;
    bottom: 18.75%;
}
.Pixso-symbol-5578_149511 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149512 {
    width: 81.27%;
    height: 59.39%;
    background-image: url(@/assets/images/Vector39.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.93%;
    right: 7.8%;
    top: 23.43%;
    bottom: 17.18%;
}
.Pixso-symbol-5578_149513 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149514 {
    width: 81.24%;
    height: 68.74%;
    background-image: url(@/assets/images/Vector40.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 15.63%;
    bottom: 15.63%;
}
</style>
