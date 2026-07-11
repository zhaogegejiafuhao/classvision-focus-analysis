<template>
    <div class="component-5572_73853">
        <div id="5572_73853" class="Pixso-symbol-5572_73853">
            <div
                id="5569_17873"
                class="Pixso-symbol-5569_17873"
                v-if="IsDarkMode === 'False'"
            >
                <slot name="slot_5572_73326">
                    <Logomark
                        id="5572_73326"
                        class="Pixso-instance-5572_73326"
                        Background="Gradient"
                    />
                </slot>
                <slot name="slot_5490_11743">
                    <div id="5490_11743" class="Pixso-vector-5490_11743"></div>
                </slot>
            </div>
            <div
                id="5572_73852"
                class="Pixso-symbol-5572_73852"
                v-if="IsDarkMode === 'True'"
            >
                <slot name="slot_5572_73848">
                    <Logomark
                        id="5572_73848"
                        class="Pixso-instance-5572_73848"
                        Background="Gradient"
                    />
                </slot>
                <slot name="slot_5572_73849">
                    <div id="5572_73849" class="Pixso-vector-5572_73849"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import Logomark from "@/components/Logomark.vue";
const props = defineProps({
    IsDarkMode: { type: String }
});
</script>
<style>
.Pixso-symbol-5572_73853 {
}
.Pixso-symbol-5569_17873 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5572_73326 {
    width: 32px;
    height: 32px;
}
.Pixso-vector-5490_11743 {
    width: 69px;
    height: 17px;
    background-image: url(@/assets/images/Vector128.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}
.Pixso-symbol-5572_73852 {
    width: auto;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5572_73848 {
    width: 32px;
    height: 32px;
}
.Pixso-vector-5572_73849 {
    width: 69px;
    height: 17px;
    background-image: url(@/assets/images/Vector127.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: relative;
    flex-shrink: 0;
}

.Pixso-instance-5572_73326 .Pixso-rectangle-5572_72548 {
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
.Pixso-instance-5572_73326 .Pixso-symbol-5572_73147 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5572_73848 .Pixso-rectangle-5572_72548 {
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
.Pixso-instance-5572_73848 .Pixso-symbol-5572_73147 .Pixso-symbol-5572_73168 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
.Pixso-instance-5572_73848 .Pixso-symbol-5572_73147 {
    width: 32px;
    height: 32px;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    gap: 5px;
    justify-content: center;
    align-items: center;
    border-radius: 12px 12px 12px 12px;
    box-shadow: 0px 4px 8px 0px rgba(79, 70, 229, 0.1);
}
</style>
