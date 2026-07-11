<template>
    <div class="component-5522_33736">
        <div id="5522_33736" class="Pixso-symbol-5522_33736">
            <div
                id="5522_33735"
                class="Pixso-symbol-5522_33735"
                v-if="DividerType === 'Icon'"
            >
                <slot name="slot_5522_33723">
                    <CaretRight
                        id="5522_33723"
                        class="Pixso-instance-5522_33723"
                        Format="Outline"
                        Weight="Bold"
                    />
                </slot>
            </div>
            <div
                id="5522_33731"
                class="Pixso-symbol-5522_33731"
                v-if="DividerType === 'Slash'"
            >
                <slot name="slot_5522_33729">
                    <p
                        id="5522_33729"
                        class="Pixso-paragraph-5522_33729 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "/" }}
                    </p>
                </slot>
            </div>
            <div
                id="5522_33737"
                class="Pixso-symbol-5522_33737"
                v-if="DividerType === 'Colon'"
            >
                <slot name="slot_5522_33738">
                    <p
                        id="5522_33738"
                        class="Pixso-paragraph-5522_33738 fill-gray30-35_1481-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ ":" }}
                    </p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import CaretRight from "@/components/Caretright.vue";
const props = defineProps({
    instance_5594_15: { type: String, default: "Component_5577_144074" },
    DividerType: { type: String }
});
</script>
<style>
.Pixso-symbol-5522_33736 {
}
.Pixso-symbol-5522_33735 {
    width: 20px;
    height: 20px;
    position: relative;
    background-color: transparent;
}
.Pixso-instance-5522_33723 {
    width: 19.999998px;
    height: 19.999998px;
}
.Pixso-symbol-5522_33731 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-paragraph-5522_33729 {
    text-align: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5522_33737 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 0px 0px 4px 0px;
    background-color: transparent;
}
.Pixso-paragraph-5522_33738 {
    text-align: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}

.Pixso-instance-5522_33723 .Pixso-symbol-5577_144074 {
    width: 19.999998px;
    height: 19.999998px;
    position: absolute;
    left: 0px;
    top: 0px;
    background-color: transparent;
}
.Pixso-instance-5522_33723 .Pixso-vector-5577_144075 {
    width: 40.65%;
    height: 71.89%;
    position: absolute;
    left: 32.8%;
    right: 26.55%;
    top: 14.05%;
    bottom: 14.06%;
}
</style>
