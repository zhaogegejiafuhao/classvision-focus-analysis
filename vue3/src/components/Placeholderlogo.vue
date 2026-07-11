<template>
    <div class="component-5579_155608">
        <div id="5579_155608" class="Pixso-symbol-5579_155608">
            <div
                id="5579_155605"
                class="Pixso-symbol-5579_155605 fill-brand10-1257_33461"
                v-if="Company === 'planetx' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155209">
                    <PlaceholderLogo
                        id="5579_155209"
                        class="Pixso-instance-5579_155209"
                        Company="planetx"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5461_42336"
                class="Pixso-symbol-5461_42336"
                v-if="Company === 'planetx' && Type === 'Logomark'"
            >
                <slot name="slot_5461_42328">
                    <div id="5461_42328" class="Pixso-vector-5461_42328"></div>
                </slot>
                <slot name="slot_5461_42329">
                    <div id="5461_42329" class="Pixso-vector-5461_42329"></div>
                </slot>
            </div>
            <div
                id="5461_42302"
                class="Pixso-symbol-5461_42302"
                v-if="Company === 'planetx' && Type === 'Logo'"
            >
                <slot name="slot_5461_42337">
                    <PlaceholderLogo
                        id="5461_42337"
                        class="Pixso-instance-5461_42337"
                        Company="planetx"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5461_42561">
                    <div id="5461_42561" class="Pixso-vector-5461_42561"></div>
                </slot>
            </div>
            <div
                id="5579_155603"
                class="Pixso-symbol-5579_155603 fill-purple10-1257_33599"
                v-if="Company === 'linez' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155204">
                    <PlaceholderLogo
                        id="5579_155204"
                        class="Pixso-instance-5579_155204"
                        Company="linez"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5461_41692"
                class="Pixso-symbol-5461_41692"
                v-if="Company === 'linez' && Type === 'Logomark'"
            >
                <div
                    id="5579_155146"
                    class="Pixso-rectangle-5579_155146 fill-purple50-1257_33603"
                ></div>
                <div
                    id="5579_155150"
                    class="Pixso-rectangle-5579_155150 fill-purple70-1257_33605"
                ></div>
                <div
                    id="5579_155191"
                    class="Pixso-rectangle-5579_155191 fill-purple70-1257_33605"
                ></div>
                <div
                    id="5579_155157"
                    class="Pixso-rectangle-5579_155157 fill-purple50-1257_33603"
                ></div>
            </div>
            <div
                id="5461_42305"
                class="Pixso-symbol-5461_42305"
                v-if="Company === 'linez' && Type === 'Logo'"
            >
                <slot name="slot_5461_42341">
                    <PlaceholderLogo
                        id="5461_42341"
                        class="Pixso-instance-5461_42341"
                        Company="linez"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5579_155168">
                    <div
                        id="5579_155168"
                        class="Pixso-vector-5579_155168"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155601"
                class="Pixso-symbol-5579_155601 fill-success10-1636_81201"
                v-if="Company === 'blox' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155297">
                    <PlaceholderLogo
                        id="5579_155297"
                        class="Pixso-instance-5579_155297"
                        Company="blox"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5461_42353"
                class="Pixso-symbol-5461_42353"
                v-if="Company === 'blox' && Type === 'Logomark'"
            >
                <div
                    id="5461_42455"
                    class="Pixso-rectangle-5461_42455 fill-success50-1636_81205"
                ></div>
                <div
                    id="5461_42472"
                    class="Pixso-rectangle-5461_42472 fill-success50-1636_81205"
                ></div>
                <slot name="slot_5579_155281">
                    <div
                        id="5579_155281"
                        class="Pixso-vector-5579_155281"
                    ></div>
                </slot>
            </div>
            <div
                id="5461_42306"
                class="Pixso-symbol-5461_42306"
                v-if="Company === 'blox' && Type === 'Logo'"
            >
                <slot name="slot_5461_42354">
                    <PlaceholderLogo
                        id="5461_42354"
                        class="Pixso-instance-5461_42354"
                        Company="blox"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5461_42558">
                    <div id="5461_42558" class="Pixso-vector-5461_42558"></div>
                </slot>
            </div>
            <div
                id="5579_155600"
                class="Pixso-symbol-5579_155600 fill-orange10-5571_38374"
                v-if="Company === 'pwrup' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155364">
                    <PlaceholderLogo
                        id="5579_155364"
                        class="Pixso-instance-5579_155364"
                        Company="pwrup"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5461_42392"
                class="Pixso-symbol-5461_42392"
                v-if="Company === 'pwrup' && Type === 'Logomark'"
            >
                <slot name="slot_5579_155305">
                    <div
                        id="5579_155305"
                        class="Pixso-vector-5579_155305"
                    ></div>
                </slot>
                <slot name="slot_5579_155306">
                    <div
                        id="5579_155306"
                        class="Pixso-vector-5579_155306"
                    ></div>
                </slot>
            </div>
            <div
                id="5461_42370"
                class="Pixso-symbol-5461_42370"
                v-if="Company === 'pwrup' && Type === 'Logo'"
            >
                <slot name="slot_5579_155335">
                    <PlaceholderLogo
                        id="5579_155335"
                        class="Pixso-instance-5579_155335"
                        Company="pwrup"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5579_155308">
                    <div
                        id="5579_155308"
                        class="Pixso-vector-5579_155308"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155604"
                class="Pixso-symbol-5579_155604 fill-teal10-5442_12422"
                v-if="Company === 'ring' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155409">
                    <PlaceholderLogo
                        id="5579_155409"
                        class="Pixso-instance-5579_155409"
                        Company="ring"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5461_42526"
                class="Pixso-symbol-5461_42526"
                v-if="Company === 'ring' && Type === 'Logomark'"
            >
                <slot name="slot_5579_155373">
                    <div
                        id="5579_155373"
                        class="Pixso-vector-5579_155373"
                    ></div>
                </slot>
                <slot name="slot_5579_155404">
                    <div
                        id="5579_155404"
                        class="Pixso-vector-5579_155404"
                    ></div>
                </slot>
            </div>
            <div
                id="5461_42301"
                class="Pixso-symbol-5461_42301"
                v-if="Company === 'ring' && Type === 'Logo'"
            >
                <slot name="slot_5461_42532">
                    <PlaceholderLogo
                        id="5461_42532"
                        class="Pixso-instance-5461_42532"
                        Company="ring"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5579_155396">
                    <div
                        id="5579_155396"
                        class="Pixso-vector-5579_155396"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155599"
                class="Pixso-symbol-5579_155599 fill-pink10-5442_12412"
                v-if="Company === 'brotha' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155450">
                    <PlaceholderLogo
                        id="5579_155450"
                        class="Pixso-instance-5579_155450"
                        Company="brotha"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5579_155425"
                class="Pixso-symbol-5579_155425"
                v-if="Company === 'brotha' && Type === 'Logomark'"
            >
                <slot name="slot_5579_155422">
                    <div
                        id="5579_155422"
                        class="Pixso-vector-5579_155422"
                    ></div>
                </slot>
                <slot name="slot_5579_155424">
                    <div
                        id="5579_155424"
                        class="Pixso-vector-5579_155424"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155607"
                class="Pixso-symbol-5579_155607"
                v-if="Company === 'brotha' && Type === 'Logo'"
            >
                <slot name="slot_5579_155443">
                    <PlaceholderLogo
                        id="5579_155443"
                        class="Pixso-instance-5579_155443"
                        Company="brotha"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5579_155432">
                    <div
                        id="5579_155432"
                        class="Pixso-vector-5579_155432"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155602"
                class="Pixso-symbol-5579_155602 fill-brand10-1257_33461"
                v-if="Company === 'zeero' && Type === 'Logo Contained'"
            >
                <slot name="slot_5579_155486">
                    <PlaceholderLogo
                        id="5579_155486"
                        class="Pixso-instance-5579_155486"
                        Company="zeero"
                        Type="Logomark"
                    />
                </slot>
            </div>
            <div
                id="5579_155481"
                class="Pixso-symbol-5579_155481"
                v-if="Company === 'zeero' && Type === 'Logomark'"
            >
                <slot name="slot_5579_155475">
                    <div
                        id="5579_155475"
                        class="Pixso-vector-5579_155475"
                    ></div>
                </slot>
                <slot name="slot_5579_155476">
                    <div
                        id="5579_155476"
                        class="Pixso-vector-5579_155476"
                    ></div>
                </slot>
                <slot name="slot_5579_155477">
                    <div
                        id="5579_155477"
                        class="Pixso-vector-5579_155477"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_155606"
                class="Pixso-symbol-5579_155606"
                v-if="Company === 'zeero' && Type === 'Logo'"
            >
                <slot name="slot_5579_155492">
                    <PlaceholderLogo
                        id="5579_155492"
                        class="Pixso-instance-5579_155492"
                        Company="zeero"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5579_155480">
                    <div
                        id="5579_155480"
                        class="Pixso-vector-5579_155480"
                    ></div>
                </slot>
            </div>
            <div
                id="5641_1474"
                class="Pixso-symbol-5641_1474 fill-lime10-5442_12700"
                v-if="Company === 'layerz' && Type === 'Logo Contained'"
            >
                <div id="5641_1470" class="Pixso-frame-5641_1470">
                    <div id="5641_1473" class="Pixso-group-5641_1473">
                        <slot name="slot_5641_1471">
                            <div
                                id="5641_1471"
                                class="Pixso-vector-5641_1471"
                            ></div>
                        </slot>
                        <slot name="slot_5641_1472">
                            <div
                                id="5641_1472"
                                class="Pixso-vector-5641_1472"
                            ></div>
                        </slot>
                    </div>
                </div>
            </div>
            <div
                id="5641_1450"
                class="Pixso-symbol-5641_1450"
                v-if="Company === 'layerz' && Type === 'Logomark'"
            >
                <slot name="slot_5641_1461">
                    <div id="5641_1461" class="Pixso-vector-5641_1461"></div>
                </slot>
                <slot name="slot_5641_1464">
                    <div id="5641_1464" class="Pixso-vector-5641_1464"></div>
                </slot>
            </div>
            <div
                id="5641_1446"
                class="Pixso-symbol-5641_1446"
                v-if="Company === 'layerz' && Type === 'Logo'"
            >
                <slot name="slot_5641_1451">
                    <PlaceholderLogo
                        id="5641_1451"
                        class="Pixso-instance-5641_1451"
                        Company="layerz"
                        Type="Logomark"
                    />
                </slot>
                <slot name="slot_5641_1442">
                    <div id="5641_1442" class="Pixso-vector-5641_1442"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import PlaceholderLogo from "@/components/Placeholderlogo.vue";
const props = defineProps({
    Company: { type: String },
    Type: { type: String }
});
</script>
<style>
.Pixso-symbol-5579_155608 {
}
.Pixso-symbol-5579_155605 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155209 {
    width: 32px;
    height: 31.999998px;
}
.Pixso-symbol-5461_42336 {
    width: 48px;
    height: 47.999996px;
    position: relative;
}
.Pixso-vector-5461_42328 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector136.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 0.000001999999998503199px));
}
.Pixso-vector-5461_42329 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector135.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 0.000001999999998503199px));
}
.Pixso-symbol-5461_42302 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5461_42337 {
    width: 48px;
    height: 47.999996px;
}
.Pixso-vector-5461_42561 {
    width: 102.59597778320312px;
    height: 28px;
    background-image: url(@/assets/images/planetX.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155603 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155204 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5461_41692 {
    width: 48px;
    height: 48px;
    position: relative;
}
.Pixso-rectangle-5579_155146 {
    width: 48px;
    height: 8px;
    position: absolute;
    left: 50%;
    top: 8px;
    transform: translateX(calc(-50% + 0px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-rectangle-5579_155150 {
    width: 28px;
    height: 8px;
    position: absolute;
    left: 50%;
    top: 20px;
    transform: translateX(calc(-50% + 10px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-rectangle-5579_155191 {
    width: 19px;
    height: 8px;
    position: absolute;
    left: 50%;
    top: 20px;
    transform: translateX(calc(-50% + -15.5px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-rectangle-5579_155157 {
    width: 48px;
    height: 8px;
    position: absolute;
    right: 0px;
    top: 32px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-symbol-5461_42305 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5461_42341 {
    width: 48px;
    height: 48px;
}
.Pixso-vector-5579_155168 {
    width: 69.81698608398438px;
    height: 28px;
    background-image: url(@/assets/images/linez.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155601 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155297 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5461_42353 {
    width: 48px;
    height: 48px;
    position: relative;
}
.Pixso-rectangle-5461_42455 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-rectangle-5461_42472 {
    width: 32px;
    height: 32px;
    position: absolute;
    right: 0px;
    bottom: 0px;
}
.Pixso-vector-5579_155281 {
    width: 16px;
    height: 16px;
    background-image: url(@/assets/images/Vector134.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16px;
    top: 16px;
}
.Pixso-symbol-5461_42306 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5461_42354 {
    width: 48px;
    height: 48px;
}
.Pixso-vector-5461_42558 {
    width: 61.21673583984375px;
    height: 24px;
    background-image: url(@/assets/images/blox.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155600 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155364 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5461_42392 {
    width: 48px;
    height: 48px;
    position: relative;
}
.Pixso-vector-5579_155305 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector133.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    bottom: 0px;
}
.Pixso-vector-5579_155306 {
    width: 24px;
    height: 24px;
    background-image: url(@/assets/images/Vector132.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 24px;
    bottom: 0px;
}
.Pixso-symbol-5461_42370 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5579_155335 {
    width: 48px;
    height: 48px;
}
.Pixso-vector-5579_155308 {
    width: 109.77764892578125px;
    height: 28px;
    background-image: url(@/assets/images/pwrup.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155604 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155409 {
    width: 32px;
    height: 32px;
}
.Pixso-symbol-5461_42526 {
    width: 48px;
    height: 48px;
    position: relative;
}
.Pixso-vector-5579_155373 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector147.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-vector-5579_155404 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector146.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-symbol-5461_42301 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5461_42532 {
    width: 48px;
    height: 48px;
}
.Pixso-vector-5579_155396 {
    width: 82.57855224609375px;
    height: 20px;
    background-image: url(@/assets/images/RING.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155599 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155450 {
    width: 32px;
    height: 31.999998px;
}
.Pixso-symbol-5579_155425 {
    width: 48px;
    height: 47.999996px;
    position: relative;
}
.Pixso-vector-5579_155422 {
    width: 48px;
    height: 24px;
    background-image: url(@/assets/images/Vector145.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-vector-5579_155424 {
    width: 48px;
    height: 24px;
    background-image: url(@/assets/images/Vector144.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    bottom: -0.000003999999997006398px;
}
.Pixso-symbol-5579_155607 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5579_155443 {
    width: 48px;
    height: 47.999996px;
}
.Pixso-vector-5579_155432 {
    width: 88.70611572265625px;
    height: 24px;
    background-image: url(@/assets/images/brotha.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5579_155602 {
    width: 48px;
    height: 48px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-instance-5579_155486 {
    width: 32px;
    height: 31.999998px;
}
.Pixso-symbol-5579_155481 {
    width: 48px;
    height: 47.999996px;
    position: relative;
}
.Pixso-vector-5579_155475 {
    width: 48px;
    height: 16px;
    background-image: url(@/assets/images/Vector143.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-vector-5579_155476 {
    width: 48px;
    height: 16px;
    background-image: url(@/assets/images/Vector142.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    bottom: -0.000003999999997006398px;
}
.Pixso-vector-5579_155477 {
    width: 48px;
    height: 48px;
    background-image: url(@/assets/images/Vector141.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0px;
    bottom: -0.000003999999997006398px;
}
.Pixso-symbol-5579_155606 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;
}
.Pixso-instance-5579_155492 {
    width: 48px;
    height: 47.999996px;
}
.Pixso-vector-5579_155480 {
    width: 86.836669921875px;
    height: 20px;
    background-image: url(@/assets/images/zeero.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5641_1474 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    border-radius: 12px 12px 12px 12px;
}
.Pixso-frame-5641_1470 {
    width: 48px;
    height: 47.999996px;
    position: absolute;
    left: -1px;
    top: 0px;
}
.Pixso-group-5641_1473 {
    width: 36.244038px;
    height: 34px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0.12199600000000244px))
        translateY(calc(-50% + 0.000001999999998503199px));
}
.Pixso-vector-5641_1471 {
    width: 36.2440185546875px;
    height: 22.702667236328125px;
    background-image: url(@/assets/images/Vector140.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.00001872265625095065px))
        translateY(calc(-50% + 5.648654618164063px));
}
.Pixso-vector-5641_1472 {
    width: 36.2440185546875px;
    height: 22.702667236328125px;
    background-image: url(@/assets/images/Vector139.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.000009722656251653916px))
        translateY(calc(-50% + -5.6486663818359375px));
}
.Pixso-symbol-5641_1450 {
    width: 48px;
    height: 47.999996px;
    position: relative;
}
.Pixso-vector-5641_1461 {
    width: 48.1229248046875px;
    height: 30.1434326171875px;
    background-image: url(@/assets/images/Vector138.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.000001597656250424545px))
        translateY(calc(-50% + 7.000014308593746px));
}
.Pixso-vector-5641_1464 {
    width: 48.1229248046875px;
    height: 30.1434326171875px;
    background-image: url(@/assets/images/Vector137.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + -0.000001597656250424545px))
        translateY(calc(-50% + -7.999984691406251px));
}
.Pixso-symbol-5641_1446 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5641_1451 {
    width: 48px;
    height: 47.999996px;
}
.Pixso-vector-5641_1442 {
    width: 79.20538330078125px;
    height: 28px;
    background-image: url(@/assets/images/layerz.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}

.Pixso-instance-5579_155209 .Pixso-symbol-5461_42336 {
    width: 32px;
    height: 31.999998px;
    position: absolute;
    left: 8px;
    top: 7.999998px;
}
.Pixso-instance-5579_155209 .Pixso-vector-5461_42328 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 9.999999992515995e-7px));
}
.Pixso-instance-5579_155209 .Pixso-vector-5461_42329 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px))
        translateY(calc(-50% + 9.999999992515995e-7px));
}
.Pixso-instance-5461_42337 .Pixso-symbol-5461_42336 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155204 .Pixso-symbol-5461_41692 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 8px;
    top: 8px;
}
.Pixso-instance-5579_155204 .Pixso-rectangle-5579_155146 {
    width: 32px;
    height: 5.333333px;
    position: absolute;
    left: 50%;
    top: 5.333333px;
    transform: translateX(calc(-50% + 0px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5579_155204 .Pixso-rectangle-5579_155150 {
    width: 18.666668px;
    height: 5.333333px;
    position: absolute;
    left: 50%;
    top: 13.333334px;
    transform: translateX(calc(-50% + 6.666668000000001px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5579_155204 .Pixso-rectangle-5579_155191 {
    width: 12.666667px;
    height: 5.333333px;
    position: absolute;
    left: 50%;
    top: 13.333334px;
    transform: translateX(calc(-50% + -10.333333499999998px));
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5579_155204 .Pixso-rectangle-5579_155157 {
    width: 32px;
    height: 5.333333px;
    position: absolute;
    right: 0px;
    top: 21.333334px;
    border-radius: 123px 123px 123px 123px;
}
.Pixso-instance-5461_42341 .Pixso-symbol-5461_41692 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155297 .Pixso-symbol-5461_42353 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 8px;
    top: 8px;
}
.Pixso-instance-5579_155297 .Pixso-rectangle-5461_42455 {
    width: 21.333334px;
    height: 21.333334px;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-instance-5579_155297 .Pixso-rectangle-5461_42472 {
    width: 21.333334px;
    height: 21.333334px;
    position: absolute;
    right: -0.0000010000000010279564px;
    bottom: -0.0000010000000010279564px;
}
.Pixso-instance-5579_155297 .Pixso-vector-5579_155281 {
    width: 10.666667px;
    height: 10.666667px;
    position: absolute;
    left: 10.666667px;
    top: 10.666667px;
}
.Pixso-instance-5461_42354 .Pixso-symbol-5461_42353 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155364 .Pixso-symbol-5461_42392 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 8px;
    top: 8px;
}
.Pixso-instance-5579_155364 .Pixso-vector-5579_155305 {
    width: 32.000004px;
    height: 31.999996px;
    position: absolute;
    left: 32px;
    bottom: 0.000004000000000559112px;
}
.Pixso-instance-5579_155364 .Pixso-vector-5579_155306 {
    width: 16.000006px;
    height: 16px;
    position: absolute;
    left: 32px;
    bottom: 0px;
}
.Pixso-instance-5579_155335 .Pixso-symbol-5461_42392 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155409 .Pixso-symbol-5461_42526 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 8px;
    top: 8px;
}
.Pixso-instance-5579_155409 .Pixso-vector-5579_155373 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-5579_155409 .Pixso-vector-5579_155404 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translateX(calc(-50% + 0px)) translateY(calc(-50% + 0px));
}
.Pixso-instance-5461_42532 .Pixso-symbol-5461_42526 {
    width: 48px;
    height: 48px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155450 .Pixso-symbol-5579_155425 {
    width: 32px;
    height: 31.999998px;
    position: absolute;
    left: 8px;
    top: 7.999998px;
}
.Pixso-instance-5579_155450 .Pixso-vector-5579_155422 {
    width: 32px;
    height: 16px;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-instance-5579_155450 .Pixso-vector-5579_155424 {
    width: 32px;
    height: 16px;
    position: absolute;
    left: 0px;
    bottom: -0.000001999999998503199px;
}
.Pixso-instance-5579_155443 .Pixso-symbol-5579_155425 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5579_155486 .Pixso-symbol-5579_155481 {
    width: 32px;
    height: 31.999998px;
    position: absolute;
    left: 8px;
    top: 7.999998px;
}
.Pixso-instance-5579_155486 .Pixso-vector-5579_155475 {
    width: 32px;
    height: 10.666667px;
    position: absolute;
    left: 0px;
    top: 0px;
}
.Pixso-instance-5579_155486 .Pixso-vector-5579_155476 {
    width: 32px;
    height: 10.666667px;
    position: absolute;
    left: 0px;
    bottom: -0.0000029999999995311555px;
}
.Pixso-instance-5579_155486 .Pixso-vector-5579_155477 {
    width: 32px;
    height: 32px;
    position: absolute;
    left: 0px;
    bottom: -0.000001999999998503199px;
}
.Pixso-instance-5579_155492 .Pixso-symbol-5579_155481 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5641_1451 .Pixso-symbol-5641_1450 {
    width: 48px;
    height: 47.999996px;
    position: relative;
    flex-shrink: 0;
}
</style>
