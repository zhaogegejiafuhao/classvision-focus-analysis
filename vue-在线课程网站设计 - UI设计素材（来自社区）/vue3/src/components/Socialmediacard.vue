<template>
    <div class="component-46_285">
        <div id="46_285" class="Pixso-symbol-46_285">
            <div
                id="46_286"
                class="stroke-wrapper-46_286"
                v-if="Property1 === 'Normal'"
            >
                <div
                    class="Pixso-symbol-46_286 fill-2nd-primary50-59_1538 fill-primary50-5_70"
                >
                    <slot name="slot_46_287">
                        <SocialMedialogo
                            id="46_287"
                            class="Pixso-instance-46_287"
                            Property1="behance 1"
                        />
                    </slot>
                </div>
                <div
                    class="stroke-46_286 stroke-primaryprimary-500-46_271"
                ></div>
            </div>
            <div
                id="46_288"
                class="Pixso-symbol-46_288 fill-primaryprimary-500-46_271"
                v-if="Property1 === 'Hover'"
            >
                <slot name="slot_46_289">
                    <SocialMedialogo
                        id="46_289"
                        class="Pixso-instance-46_289"
                        Property1="behance 1"
                    />
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import SocialMedialogo from "@/components/Socialmedialogo.vue";
const props = defineProps({
    Property1: { type: String }
});
</script>
<style>
.Pixso-symbol-46_285 {
}
.Pixso-symbol-46_286 {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: center;
    padding: 14px 14px 14px 14px;
    border-radius: 4px 4px 4px 4px;
}
.stroke-wrapper-46_286 {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
}
.stroke-46_286 {
    position: absolute;
    inset: 0px;
    border-radius: 4px 4px 4px 4px;
    pointer-events: none;
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-46_287 {
    width: 20px;
    height: 20px;
}
.Pixso-symbol-46_288 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    padding: 14px 14px 14px 14px;
    border-radius: 4px 4px 4px 4px;
}
.Pixso-instance-46_289 {
    width: 20px;
    height: 20px;
}

.Pixso-instance-46_287 .Pixso-symbol-46_274 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-46_289 .Pixso-symbol-46_274 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    background-color: transparent;
}
.Pixso-instance-46_287 .Pixso-vector-46_275 {
    width: 99.98%;
    height: 62.5%;
    position: absolute;
    left: 0%;
    right: 0.02%;
    top: 16.67%;
    bottom: 20.83%;
}
.Pixso-instance-46_289 .Pixso-vector-46_275 {
    width: 99.98%;
    height: 62.5%;
    position: absolute;
    left: 0%;
    right: 0.02%;
    top: 16.67%;
    bottom: 20.83%;
}
.Pixso-instance-46_287 .Pixso-symbol-46_274 .Pixso-symbol-46_276 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 24px)) translateY(calc(-50% + 24px));
    background-color: transparent;
}
.Pixso-instance-46_287 .Pixso-symbol-46_274 .Pixso-symbol-46_278 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 24px)) translateY(calc(-50% + 24px));
    background-color: transparent;
}
.Pixso-instance-46_287 .Pixso-symbol-46_274 .Pixso-symbol-46_280 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 24px)) translateY(calc(-50% + 24px));
    background-color: transparent;
}
.Pixso-instance-46_287 .Pixso-symbol-46_274 .Pixso-symbol-46_282 {
    width: 20px;
    height: 20px;
    overflow: hidden;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 24px)) translateY(calc(-50% + 24px));
    background-color: transparent;
}
</style>
