<template>
    <div class="component-5464_43238">
        <div id="5464_43238" class="Pixso-symbol-5464_43238">
            <div
                id="5464_43239"
                class="stroke-wrapper-5464_43239"
                v-if="Size === 'xs'"
            >
                <div
                    class="Pixso-symbol-5464_43239 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2067">
                        <PlaceholderLogo
                            id="5471_2067"
                            class="Pixso-instance-5471_2067"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43239 stroke-gray0-white-67_3285"></div>
            </div>
            <div
                id="5464_43240"
                class="stroke-wrapper-5464_43240"
                v-if="Size === 'sm'"
            >
                <div
                    class="Pixso-symbol-5464_43240 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2060">
                        <PlaceholderLogo
                            id="5471_2060"
                            class="Pixso-instance-5471_2060"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43240 stroke-gray0-white-67_3285"></div>
            </div>
            <div
                id="5464_43241"
                class="stroke-wrapper-5464_43241"
                v-if="Size === 'md'"
            >
                <div
                    class="Pixso-symbol-5464_43241 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2056">
                        <PlaceholderLogo
                            id="5471_2056"
                            class="Pixso-instance-5471_2056"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43241 stroke-gray0-white-67_3285"></div>
            </div>
            <div
                id="5464_43242"
                class="stroke-wrapper-5464_43242"
                v-if="Size === 'lg'"
            >
                <div
                    class="Pixso-symbol-5464_43242 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2052">
                        <PlaceholderLogo
                            id="5471_2052"
                            class="Pixso-instance-5471_2052"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43242 stroke-gray0-white-67_3285"></div>
            </div>
            <div
                id="5464_43243"
                class="stroke-wrapper-5464_43243"
                v-if="Size === 'xl'"
            >
                <div
                    class="Pixso-symbol-5464_43243 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2048">
                        <PlaceholderLogo
                            id="5471_2048"
                            class="Pixso-instance-5471_2048"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43243 stroke-gray0-white-67_3285"></div>
            </div>
            <div
                id="5464_43244"
                class="stroke-wrapper-5464_43244"
                v-if="Size === '2xl'"
            >
                <div
                    class="Pixso-symbol-5464_43244 fill-brand10-1257_33461 fill-brand5-1257_33460"
                >
                    <slot name="slot_5471_2044">
                        <PlaceholderLogo
                            id="5471_2044"
                            class="Pixso-instance-5471_2044"
                            Company="planetx"
                            Type="Logomark"
                        />
                    </slot>
                </div>
                <div class="stroke-5464_43244 stroke-gray0-white-67_3285"></div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import PlaceholderLogo from "@/components/Placeholderlogo.vue";
const props = defineProps({
    Size: { type: String }
});
</script>
<style>
.Pixso-symbol-5464_43238 {
}
.Pixso-symbol-5464_43239 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5464_43239 {
    position: relative;
    width: 10px;
    height: 10px;
    display: flex;
}
.stroke-5464_43239 {
    position: absolute;
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2067 {
    width: 6.000001px;
    height: 6px;
}
.Pixso-symbol-5464_43240 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5464_43240 {
    position: relative;
    width: 12px;
    height: 12px;
    display: flex;
}
.stroke-5464_43240 {
    position: absolute;
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2060 {
    width: 6.000001px;
    height: 6px;
}
.Pixso-symbol-5464_43241 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5464_43241 {
    position: relative;
    width: 14px;
    height: 14px;
    display: flex;
}
.stroke-5464_43241 {
    position: absolute;
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2056 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5464_43242 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
}
.stroke-wrapper-5464_43242 {
    position: relative;
    width: 16px;
    height: 16px;
    display: flex;
}
.stroke-5464_43242 {
    position: absolute;
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2052 {
    width: 10px;
    height: 9.999999px;
}
.Pixso-symbol-5464_43243 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-image: url(@/assets/images/e8aa5d3a3d822909dd3c274e5ac1c80ef63111a4.png);
}
.stroke-wrapper-5464_43243 {
    position: relative;
    width: 18px;
    height: 18px;
    display: flex;
}
.stroke-5464_43243 {
    position: absolute;
    inset: -1.5px -1.5px -1.5px -1.5px;
    border-radius: 13.5px 13.5px 13.5px 13.5px;
    pointer-events: none;
    border-width: 1.5px 1.5px 1.5px 1.5px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2048 {
    width: 12px;
    height: 11.999999px;
}
.Pixso-symbol-5464_43244 {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border-radius: 1234px 1234px 1234px 1234px;
}
.stroke-wrapper-5464_43244 {
    position: relative;
    width: 20px;
    height: 20px;
    display: flex;
}
.stroke-5464_43244 {
    position: absolute;
    inset: -1.666667px -1.666667px -1.666667px -1.666667px;
    border-radius: 1235.666667px 1235.666667px 1235.666667px 1235.666667px;
    pointer-events: none;
    border-width: 1.666667px 1.666667px 1.666667px 1.666667px;
    border-style: solid;
    box-sizing: border-box;
}
.Pixso-instance-5471_2044 {
    width: 12px;
    height: 11.999999px;
}

.Pixso-instance-5471_2067 .Pixso-symbol-5461_42336 {
    width: 6.000001px;
    height: 6px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2067 .Pixso-vector-5461_42328 {
    width: 6.000001px;
    height: 6.000001px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 5.00000000069889e-7px));
}
.Pixso-instance-5471_2067 .Pixso-vector-5461_42329 {
    width: 6.000001px;
    height: 6.000001px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 5.00000000069889e-7px));
}
.Pixso-instance-5471_2060 .Pixso-symbol-5461_42336 {
    width: 6.000001px;
    height: 6px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2060 .Pixso-vector-5461_42328 {
    width: 6.000001px;
    height: 6.000001px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 5.00000000069889e-7px));
}
.Pixso-instance-5471_2060 .Pixso-vector-5461_42329 {
    width: 6.000001px;
    height: 6.000001px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 5.00000000069889e-7px));
}
.Pixso-instance-5471_2056 .Pixso-symbol-5461_42336 {
    width: 8px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2056 .Pixso-vector-5461_42328 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-5471_2056 .Pixso-vector-5461_42329 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-5471_2052 .Pixso-symbol-5461_42336 {
    width: 10px;
    height: 9.999999px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2052 .Pixso-vector-5461_42328 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
.Pixso-instance-5471_2052 .Pixso-vector-5461_42329 {
    width: 10px;
    height: 10px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
.Pixso-instance-5471_2048 .Pixso-symbol-5461_42336 {
    width: 12px;
    height: 11.999999px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2048 .Pixso-vector-5461_42328 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
.Pixso-instance-5471_2048 .Pixso-vector-5461_42329 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
.Pixso-instance-5471_2044 .Pixso-symbol-5461_42336 {
    width: 12px;
    height: 11.999999px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5471_2044 .Pixso-vector-5461_42328 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
.Pixso-instance-5471_2044 .Pixso-vector-5461_42329 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 4.999999996257998e-7px));
}
</style>
