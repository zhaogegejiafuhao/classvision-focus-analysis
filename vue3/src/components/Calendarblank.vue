<template>
    <div class="component-5578_148815">
        <div id="5578_148815" class="Pixso-symbol-5578_148815">
            <div
                id="5578_148816"
                class="Pixso-symbol-5578_148816"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_148817">
                    <div
                        id="5578_148817"
                        class="Pixso-vector-5578_148817"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148822"
                class="Pixso-symbol-5578_148822"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_148823">
                    <div
                        id="5578_148823"
                        class="Pixso-vector-5578_148823"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_148824"
                class="Pixso-symbol-5578_148824"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_148825">
                    <div
                        id="5578_148825"
                        class="Pixso-vector-5578_148825"
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
.Pixso-symbol-5578_148815 {
}
.Pixso-symbol-5578_148816 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148817 {
    width: 75%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector377.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 6.25%;
    bottom: 12.5%;
}
.Pixso-symbol-5578_148822 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148823 {
    width: 78.12%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector375.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 4.69%;
    bottom: 10.94%;
}
.Pixso-symbol-5578_148824 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_148825 {
    width: 75%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector376.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 6.25%;
    bottom: 12.5%;
}
</style>
