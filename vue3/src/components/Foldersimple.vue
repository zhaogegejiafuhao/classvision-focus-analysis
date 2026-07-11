<template>
    <div class="component-5579_151644">
        <div id="5579_151644" class="Pixso-symbol-5579_151644">
            <div
                id="5579_151645"
                class="Pixso-symbol-5579_151645"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151646">
                    <div
                        id="5579_151646"
                        class="Pixso-vector-5579_151646"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151651"
                class="Pixso-symbol-5579_151651"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151652">
                    <div
                        id="5579_151652"
                        class="Pixso-vector-5579_151652"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151653"
                class="Pixso-symbol-5579_151653"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151654">
                    <div
                        id="5579_151654"
                        class="Pixso-vector-5579_151654"
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
.Pixso-symbol-5579_151644 {
}
.Pixso-symbol-5579_151645 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151646 {
    width: 81.24%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector322.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 18.75%;
    bottom: 15.63%;
}
.Pixso-symbol-5579_151651 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151652 {
    width: 84.38%;
    height: 68.75%;
    background-image: url(@/assets/images/Vector320.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 17.19%;
    bottom: 14.06%;
}
.Pixso-symbol-5579_151653 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151654 {
    width: 81.24%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector321.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 18.75%;
    bottom: 15.63%;
}
</style>
