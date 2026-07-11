<template>
    <div class="component-5430_5950">
        <div id="5430_5950" class="Pixso-symbol-5430_5950">
            <div
                id="5430_5949"
                class="stroke-wrapper-5430_5949"
                v-if="Background === 'Black'"
            >
                <div
                    class="Pixso-symbol-5430_5949 fill-gray100-black-5502_9900"
                >
                    <slot name="slot_5572_73163">
                        <div
                            id="5572_73163"
                            class="Pixso-vector-5572_73163"
                        ></div>
                    </slot>
                </div>
                <div
                    class="stroke-5430_5949 stroke-transparentwhite32-5571_36639"
                ></div>
            </div>
            <div
                id="5572_73168"
                class="stroke-wrapper-5572_73168"
                v-if="Background === 'White'"
            >
                <div class="Pixso-symbol-5572_73168 fill-gray0-white-67_3285">
                    <slot name="slot_5572_73169">
                        <div
                            id="5572_73169"
                            class="Pixso-vector-5572_73169"
                        ></div>
                    </slot>
                </div>
                <div class="stroke-5572_73168 stroke-gray20-36_1844"></div>
            </div>
            <div
                id="1428_20616"
                class="stroke-wrapper-1428_20616"
                v-if="Background === 'Brand'"
            >
                <div class="Pixso-symbol-1428_20616 fill-brand60-1257_33467">
                    <slot name="slot_5572_73170">
                        <div
                            id="5572_73170"
                            class="Pixso-vector-5572_73170"
                        ></div>
                    </slot>
                </div>
                <div
                    class="stroke-1428_20616 stroke-transparentwhite32-5571_36639"
                ></div>
            </div>
            <div
                id="5572_73147"
                class="stroke-wrapper-5572_73147"
                v-if="Background === 'Gradient'"
            >
                <div class="Pixso-symbol-5572_73147 fill-brand60-1257_33467">
                    <div
                        id="5572_72548"
                        class="Pixso-rectangle-5572_72548"
                    ></div>
                    <slot name="slot_5572_73037">
                        <div
                            id="5572_73037"
                            class="Pixso-vector-5572_73037"
                        ></div>
                    </slot>
                </div>
                <div
                    class="stroke-5572_73147 stroke-transparentwhite32-5571_36639"
                ></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Background: { type: String }
});
</script>
<style>
.Pixso-symbol-5430_5950 {
}
.Pixso-symbol-5430_5949 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5430_5949 {
    position: relative;
    width: 32px;
    height: 32px;
    display: flex;
}
.stroke-5430_5949 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5572_73163 {
    width: 30.6201171875px;
    height: 34.5px;
    background-image: url(@/assets/images/Vector120.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5572_73168 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.stroke-wrapper-5572_73168 {
    position: relative;
    width: 32px;
    height: 32px;
    display: flex;
}
.stroke-5572_73168 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5572_73169 {
    width: 30.6201171875px;
    height: 34.5px;
    background-image: url(@/assets/images/Vector123.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-1428_20616 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.stroke-wrapper-1428_20616 {
    position: relative;
    width: 32px;
    height: 32px;
    display: flex;
}
.stroke-1428_20616 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-vector-5572_73170 {
    width: 30.6201171875px;
    height: 34.5px;
    background-image: url(@/assets/images/Vector122.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5572_73147 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.stroke-wrapper-5572_73147 {
    position: relative;
    width: 32px;
    height: 32px;
    display: flex;
}
.stroke-5572_73147 {
    position: absolute;
    inset: 0px;
    border-radius: 12px 12px 12px 12px;
    pointer-events: none;
    border-width: 0.5px 0.5px 0.5px 0.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-rectangle-5572_72548 {
    width: 61.388157px;
    height: 35.078945px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.0007412566720219615px))
        translateY(calc(-50% + 0.00005610324103955122px)) rotate(-164.999998deg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/201faa1ef50a78dda4233dc317a385f1f17ffd6c.png);
}
.Pixso-vector-5572_73037 {
    width: 30.6201171875px;
    height: 34.5px;
    background-image: url(@/assets/images/Vector121.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
</style>
