<template>
    <div class="component-5577_148215">
        <div id="5577_148215" class="Pixso-symbol-5577_148215">
            <div
                id="5577_148216"
                class="Pixso-symbol-5577_148216"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_148217">
                    <div
                        id="5577_148217"
                        class="Pixso-vector-5577_148217"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148222"
                class="Pixso-symbol-5577_148222"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_148223">
                    <div
                        id="5577_148223"
                        class="Pixso-vector-5577_148223"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_148224"
                class="Pixso-symbol-5577_148224"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_148225">
                    <div
                        id="5577_148225"
                        class="Pixso-vector-5577_148225"
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
.Pixso-symbol-5577_148215 {
}
.Pixso-symbol-5577_148216 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148217 {
    width: 68.74%;
    height: 81.26%;
    background-image: url(@/assets/images/Vector368.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 25%;
    right: 6.26%;
    top: 9.37%;
    bottom: 9.37%;
}
.Pixso-symbol-5577_148222 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148223 {
    width: 71.87%;
    height: 84.36%;
    background-image: url(@/assets/images/Vector366.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 23.44%;
    right: 4.69%;
    top: 7.82%;
    bottom: 7.82%;
}
.Pixso-symbol-5577_148224 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_148225 {
    width: 68.75%;
    height: 81.26%;
    background-image: url(@/assets/images/Vector367.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 25%;
    right: 6.25%;
    top: 9.37%;
    bottom: 9.37%;
}
</style>
