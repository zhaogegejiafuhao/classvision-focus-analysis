<template>
    <div class="component-5577_144210">
        <div id="5577_144210" class="Pixso-symbol-5577_144210">
            <div
                id="5577_144211"
                class="Pixso-symbol-5577_144211"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144212">
                    <div
                        id="5577_144212"
                        class="Pixso-vector-5577_144212"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144217"
                class="Pixso-symbol-5577_144217"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144218">
                    <div
                        id="5577_144218"
                        class="Pixso-vector-5577_144218"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144219"
                class="Pixso-symbol-5577_144219"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144220">
                    <div
                        id="5577_144220"
                        class="Pixso-vector-5577_144220"
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
.Pixso-symbol-5577_144210 {
}
.Pixso-symbol-5577_144211 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144212 {
    width: 81.25%;
    height: 74.99%;
    background-image: url(@/assets/images/Vector38.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 12.5%;
    top: 12.51%;
    bottom: 12.5%;
}
.Pixso-symbol-5577_144217 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144218 {
    width: 84.37%;
    height: 78.14%;
    background-image: url(@/assets/images/Vector36.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 10.94%;
    top: 10.92%;
    bottom: 10.94%;
}
.Pixso-symbol-5577_144219 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144220 {
    width: 81.25%;
    height: 74.99%;
    background-image: url(@/assets/images/Vector37.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 12.5%;
    top: 12.51%;
    bottom: 12.5%;
}
</style>
