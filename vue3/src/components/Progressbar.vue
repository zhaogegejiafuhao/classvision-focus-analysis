<template>
    <div class="component-1264_9860">
        <div id="1264_9860" class="Pixso-symbol-1264_9860">
            <div
                id="1264_9861"
                class="Pixso-symbol-1264_9861"
                v-if="Progression === '0' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9862" class="Pixso-frame-1264_9862">
                    <slot name="slot_1264_9863">
                        <ProgressBarAtom
                            id="1264_9863"
                            class="Pixso-instance-1264_9863"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9864">
                        <ProgressBarAtom
                            id="1264_9864"
                            class="Pixso-instance-1264_9864"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_8978"
                class="Pixso-symbol-5615_8978"
                v-if="Progression === '0' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_8979" class="Pixso-frame-5615_8979">
                    <slot name="slot_5615_8980">
                        <ProgressBarAtom
                            id="5615_8980"
                            class="Pixso-instance-5615_8980"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_8981">
                        <ProgressBarAtom
                            id="5615_8981"
                            class="Pixso-instance-5615_8981"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_9971"
                class="Pixso-symbol-1264_9971"
                v-if="
                    Progression === '0' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9972">
                    <ProgressBar
                        id="1264_9972"
                        class="Pixso-instance-1264_9972"
                        Progression="0"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43888">
                    <p
                        id="5555_43888"
                        class="Pixso-paragraph-5555_43888 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_8982"
                class="Pixso-symbol-5615_8982"
                v-if="
                    Progression === '0' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_8983">
                    <ProgressBar
                        id="5615_8983"
                        class="Pixso-instance-5615_8983"
                        Progression="0"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_8986">
                    <p
                        id="5615_8986"
                        class="Pixso-paragraph-5615_8986 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54044"
                class="Pixso-symbol-5631_54044"
                v-if="Progression === '0' && Size === 'md' && Label === 'Right'"
            >
                <slot name="slot_5631_54045">
                    <ProgressBar
                        id="5631_54045"
                        class="Pixso-instance-5631_54045"
                        Progression="0"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54046">
                    <p
                        id="5631_54046"
                        class="Pixso-paragraph-5631_54046 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54047"
                class="Pixso-symbol-5631_54047"
                v-if="Progression === '0' && Size === 'lg' && Label === 'Right'"
            >
                <slot name="slot_5631_54048">
                    <ProgressBar
                        id="5631_54048"
                        class="Pixso-instance-5631_54048"
                        Progression="0"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54049">
                    <p
                        id="5631_54049"
                        class="Pixso-paragraph-5631_54049 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9974"
                class="Pixso-symbol-1264_9974"
                v-if="
                    Progression === '10' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9975">
                    <ProgressBar
                        id="1264_9975"
                        class="Pixso-instance-1264_9975"
                        Progression="10"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43892">
                    <p
                        id="5555_43892"
                        class="Pixso-paragraph-5555_43892 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_8991"
                class="Pixso-symbol-5615_8991"
                v-if="
                    Progression === '10' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_8992">
                    <ProgressBar
                        id="5615_8992"
                        class="Pixso-instance-5615_8992"
                        Progression="10"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_8995">
                    <p
                        id="5615_8995"
                        class="Pixso-paragraph-5615_8995 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9865"
                class="Pixso-symbol-1264_9865"
                v-if="Progression === '10' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9866" class="Pixso-frame-1264_9866">
                    <slot name="slot_1264_9867">
                        <ProgressBarAtom
                            id="1264_9867"
                            class="Pixso-instance-1264_9867"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9868">
                        <ProgressBarAtom
                            id="1264_9868"
                            class="Pixso-instance-1264_9868"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_8987"
                class="Pixso-symbol-5615_8987"
                v-if="Progression === '10' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_8988" class="Pixso-frame-5615_8988">
                    <slot name="slot_5615_8989">
                        <ProgressBarAtom
                            id="5615_8989"
                            class="Pixso-instance-5615_8989"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_8990">
                        <ProgressBarAtom
                            id="5615_8990"
                            class="Pixso-instance-5615_8990"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_9977"
                class="Pixso-symbol-1264_9977"
                v-if="
                    Progression === '20' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9978">
                    <ProgressBar
                        id="1264_9978"
                        class="Pixso-instance-1264_9978"
                        Progression="20"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43895">
                    <p
                        id="5555_43895"
                        class="Pixso-paragraph-5555_43895 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9000"
                class="Pixso-symbol-5615_9000"
                v-if="
                    Progression === '20' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9001">
                    <ProgressBar
                        id="5615_9001"
                        class="Pixso-instance-5615_9001"
                        Progression="20"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9004">
                    <p
                        id="5615_9004"
                        class="Pixso-paragraph-5615_9004 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54050"
                class="Pixso-symbol-5631_54050"
                v-if="
                    Progression === '10' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54051">
                    <ProgressBar
                        id="5631_54051"
                        class="Pixso-instance-5631_54051"
                        Progression="10"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54052">
                    <p
                        id="5631_54052"
                        class="Pixso-paragraph-5631_54052 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54053"
                class="Pixso-symbol-5631_54053"
                v-if="
                    Progression === '10' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54054">
                    <ProgressBar
                        id="5631_54054"
                        class="Pixso-instance-5631_54054"
                        Progression="10"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54055">
                    <p
                        id="5631_54055"
                        class="Pixso-paragraph-5631_54055 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9980"
                class="Pixso-symbol-1264_9980"
                v-if="
                    Progression === '30' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9981">
                    <ProgressBar
                        id="1264_9981"
                        class="Pixso-instance-1264_9981"
                        Progression="30"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43908">
                    <p
                        id="5555_43908"
                        class="Pixso-paragraph-5555_43908 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9009"
                class="Pixso-symbol-5615_9009"
                v-if="
                    Progression === '30' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9010">
                    <ProgressBar
                        id="5615_9010"
                        class="Pixso-instance-5615_9010"
                        Progression="30"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9013">
                    <p
                        id="5615_9013"
                        class="Pixso-paragraph-5615_9013 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9869"
                class="Pixso-symbol-1264_9869"
                v-if="Progression === '20' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9870" class="Pixso-frame-1264_9870">
                    <slot name="slot_1264_9871">
                        <ProgressBarAtom
                            id="1264_9871"
                            class="Pixso-instance-1264_9871"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9872">
                        <ProgressBarAtom
                            id="1264_9872"
                            class="Pixso-instance-1264_9872"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_8996"
                class="Pixso-symbol-5615_8996"
                v-if="Progression === '20' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_8997" class="Pixso-frame-5615_8997">
                    <slot name="slot_5615_8998">
                        <ProgressBarAtom
                            id="5615_8998"
                            class="Pixso-instance-5615_8998"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_8999">
                        <ProgressBarAtom
                            id="5615_8999"
                            class="Pixso-instance-5615_8999"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_9983"
                class="Pixso-symbol-1264_9983"
                v-if="
                    Progression === '40' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9984">
                    <ProgressBar
                        id="1264_9984"
                        class="Pixso-instance-1264_9984"
                        Progression="40"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43911">
                    <p
                        id="5555_43911"
                        class="Pixso-paragraph-5555_43911 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9018"
                class="Pixso-symbol-5615_9018"
                v-if="
                    Progression === '40' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9019">
                    <ProgressBar
                        id="5615_9019"
                        class="Pixso-instance-5615_9019"
                        Progression="40"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9022">
                    <p
                        id="5615_9022"
                        class="Pixso-paragraph-5615_9022 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54056"
                class="Pixso-symbol-5631_54056"
                v-if="
                    Progression === '20' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54057">
                    <ProgressBar
                        id="5631_54057"
                        class="Pixso-instance-5631_54057"
                        Progression="20"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54058">
                    <p
                        id="5631_54058"
                        class="Pixso-paragraph-5631_54058 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54059"
                class="Pixso-symbol-5631_54059"
                v-if="
                    Progression === '20' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54060">
                    <ProgressBar
                        id="5631_54060"
                        class="Pixso-instance-5631_54060"
                        Progression="20"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54061">
                    <p
                        id="5631_54061"
                        class="Pixso-paragraph-5631_54061 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9986"
                class="Pixso-symbol-1264_9986"
                v-if="
                    Progression === '50' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9987">
                    <ProgressBar
                        id="1264_9987"
                        class="Pixso-instance-1264_9987"
                        Progression="50"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43914">
                    <p
                        id="5555_43914"
                        class="Pixso-paragraph-5555_43914 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9027"
                class="Pixso-symbol-5615_9027"
                v-if="
                    Progression === '50' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9028">
                    <ProgressBar
                        id="5615_9028"
                        class="Pixso-instance-5615_9028"
                        Progression="50"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9031">
                    <p
                        id="5615_9031"
                        class="Pixso-paragraph-5615_9031 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9877"
                class="Pixso-symbol-1264_9877"
                v-if="Progression === '30' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9878" class="Pixso-frame-1264_9878">
                    <slot name="slot_1264_9879">
                        <ProgressBarAtom
                            id="1264_9879"
                            class="Pixso-instance-1264_9879"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9880">
                        <ProgressBarAtom
                            id="1264_9880"
                            class="Pixso-instance-1264_9880"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_9005"
                class="Pixso-symbol-5615_9005"
                v-if="Progression === '30' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9006" class="Pixso-frame-5615_9006">
                    <slot name="slot_5615_9007">
                        <ProgressBarAtom
                            id="5615_9007"
                            class="Pixso-instance-5615_9007"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9008">
                        <ProgressBarAtom
                            id="5615_9008"
                            class="Pixso-instance-5615_9008"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_9989"
                class="Pixso-symbol-1264_9989"
                v-if="
                    Progression === '60' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9990">
                    <ProgressBar
                        id="1264_9990"
                        class="Pixso-instance-1264_9990"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43917">
                    <p
                        id="5555_43917"
                        class="Pixso-paragraph-5555_43917 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9036"
                class="Pixso-symbol-5615_9036"
                v-if="
                    Progression === '60' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9037">
                    <ProgressBar
                        id="5615_9037"
                        class="Pixso-instance-5615_9037"
                        Progression="60"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9040">
                    <p
                        id="5615_9040"
                        class="Pixso-paragraph-5615_9040 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54062"
                class="Pixso-symbol-5631_54062"
                v-if="
                    Progression === '30' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54063">
                    <ProgressBar
                        id="5631_54063"
                        class="Pixso-instance-5631_54063"
                        Progression="30"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54064">
                    <p
                        id="5631_54064"
                        class="Pixso-paragraph-5631_54064 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54065"
                class="Pixso-symbol-5631_54065"
                v-if="
                    Progression === '30' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54066">
                    <ProgressBar
                        id="5631_54066"
                        class="Pixso-instance-5631_54066"
                        Progression="30"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54067">
                    <p
                        id="5631_54067"
                        class="Pixso-paragraph-5631_54067 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9992"
                class="Pixso-symbol-1264_9992"
                v-if="
                    Progression === '70' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9993">
                    <ProgressBar
                        id="1264_9993"
                        class="Pixso-instance-1264_9993"
                        Progression="70"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43920">
                    <p
                        id="5555_43920"
                        class="Pixso-paragraph-5555_43920 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9045"
                class="Pixso-symbol-5615_9045"
                v-if="
                    Progression === '70' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9046">
                    <ProgressBar
                        id="5615_9046"
                        class="Pixso-instance-5615_9046"
                        Progression="70"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9049">
                    <p
                        id="5615_9049"
                        class="Pixso-paragraph-5615_9049 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9873"
                class="Pixso-symbol-1264_9873"
                v-if="Progression === '40' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9874" class="Pixso-frame-1264_9874">
                    <slot name="slot_1264_9875">
                        <ProgressBarAtom
                            id="1264_9875"
                            class="Pixso-instance-1264_9875"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9876">
                        <ProgressBarAtom
                            id="1264_9876"
                            class="Pixso-instance-1264_9876"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_9014"
                class="Pixso-symbol-5615_9014"
                v-if="Progression === '40' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9015" class="Pixso-frame-5615_9015">
                    <slot name="slot_5615_9016">
                        <ProgressBarAtom
                            id="5615_9016"
                            class="Pixso-instance-5615_9016 fill-gray10-83_2713 fill-gray20-36_1844"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9017">
                        <ProgressBarAtom
                            id="5615_9017"
                            class="Pixso-instance-5615_9017"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_9995"
                class="Pixso-symbol-1264_9995"
                v-if="
                    Progression === '80' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9996">
                    <ProgressBar
                        id="1264_9996"
                        class="Pixso-instance-1264_9996"
                        Progression="80"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43923">
                    <p
                        id="5555_43923"
                        class="Pixso-paragraph-5555_43923 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9054"
                class="Pixso-symbol-5615_9054"
                v-if="
                    Progression === '80' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9055">
                    <ProgressBar
                        id="5615_9055"
                        class="Pixso-instance-5615_9055"
                        Progression="80"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9058">
                    <p
                        id="5615_9058"
                        class="Pixso-paragraph-5615_9058 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54068"
                class="Pixso-symbol-5631_54068"
                v-if="
                    Progression === '40' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54069">
                    <ProgressBar
                        id="5631_54069"
                        class="Pixso-instance-5631_54069"
                        Progression="40"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54070">
                    <p
                        id="5631_54070"
                        class="Pixso-paragraph-5631_54070 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54071"
                class="Pixso-symbol-5631_54071"
                v-if="
                    Progression === '40' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54072">
                    <ProgressBar
                        id="5631_54072"
                        class="Pixso-instance-5631_54072"
                        Progression="40"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54073">
                    <p
                        id="5631_54073"
                        class="Pixso-paragraph-5631_54073 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9998"
                class="Pixso-symbol-1264_9998"
                v-if="
                    Progression === '90' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_9999">
                    <ProgressBar
                        id="1264_9999"
                        class="Pixso-instance-1264_9999"
                        Progression="90"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43926">
                    <p
                        id="5555_43926"
                        class="Pixso-paragraph-5555_43926 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9063"
                class="Pixso-symbol-5615_9063"
                v-if="
                    Progression === '90' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9064">
                    <ProgressBar
                        id="5615_9064"
                        class="Pixso-instance-5615_9064"
                        Progression="90"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9067">
                    <p
                        id="5615_9067"
                        class="Pixso-paragraph-5615_9067 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9881"
                class="Pixso-symbol-1264_9881"
                v-if="Progression === '50' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9882" class="Pixso-frame-1264_9882">
                    <slot name="slot_1264_9883">
                        <ProgressBarAtom
                            id="1264_9883"
                            class="Pixso-instance-1264_9883"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9884">
                        <ProgressBarAtom
                            id="1264_9884"
                            class="Pixso-instance-1264_9884"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_9023"
                class="Pixso-symbol-5615_9023"
                v-if="Progression === '50' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9024" class="Pixso-frame-5615_9024">
                    <slot name="slot_5615_9025">
                        <ProgressBarAtom
                            id="5615_9025"
                            class="Pixso-instance-5615_9025"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9026">
                        <ProgressBarAtom
                            id="5615_9026"
                            class="Pixso-instance-5615_9026"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="1264_10001"
                class="Pixso-symbol-1264_10001"
                v-if="
                    Progression === '100' && Size === 'md' && Label === 'Bottom'
                "
            >
                <slot name="slot_1264_10002">
                    <ProgressBar
                        id="1264_10002"
                        class="Pixso-instance-1264_10002"
                        Progression="100"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_43929">
                    <p
                        id="5555_43929"
                        class="Pixso-paragraph-5555_43929 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9072"
                class="Pixso-symbol-5615_9072"
                v-if="
                    Progression === '100' && Size === 'lg' && Label === 'Bottom'
                "
            >
                <slot name="slot_5615_9073">
                    <ProgressBar
                        id="5615_9073"
                        class="Pixso-instance-5615_9073"
                        Progression="100"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5615_9076">
                    <p
                        id="5615_9076"
                        class="Pixso-paragraph-5615_9076 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54074"
                class="Pixso-symbol-5631_54074"
                v-if="
                    Progression === '50' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54075">
                    <ProgressBar
                        id="5631_54075"
                        class="Pixso-instance-5631_54075"
                        Progression="50"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54076">
                    <p
                        id="5631_54076"
                        class="Pixso-paragraph-5631_54076 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44106"
                class="Pixso-symbol-5555_44106"
                v-if="
                    Progression === '0' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44194">
                    <ProgressBar
                        id="5555_44194"
                        class="Pixso-instance-5555_44194"
                        Progression="0"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44110">
                    <p
                        id="5555_44110"
                        class="Pixso-paragraph-5555_44110 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54077"
                class="Pixso-symbol-5631_54077"
                v-if="
                    Progression === '50' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54078">
                    <ProgressBar
                        id="5631_54078"
                        class="Pixso-instance-5631_54078"
                        Progression="50"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54079">
                    <p
                        id="5631_54079"
                        class="Pixso-paragraph-5631_54079 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44111"
                class="Pixso-symbol-5555_44111"
                v-if="
                    Progression === '10' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44198">
                    <ProgressBar
                        id="5555_44198"
                        class="Pixso-instance-5555_44198"
                        Progression="10"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44115">
                    <p
                        id="5555_44115"
                        class="Pixso-paragraph-5555_44115 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9885"
                class="Pixso-symbol-1264_9885"
                v-if="Progression === '60' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9886" class="Pixso-frame-1264_9886">
                    <slot name="slot_1264_9887">
                        <ProgressBarAtom
                            id="1264_9887"
                            class="Pixso-instance-1264_9887 fill-brand60-1257_33467 fill-gray50-35_1480"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9888">
                        <ProgressBarAtom
                            id="1264_9888"
                            class="Pixso-instance-1264_9888 fill-gray0-white-67_3285"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5555_44116"
                class="Pixso-symbol-5555_44116"
                v-if="
                    Progression === '20' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44202">
                    <ProgressBar
                        id="5555_44202"
                        class="Pixso-instance-5555_44202"
                        Progression="20"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44120">
                    <p
                        id="5555_44120"
                        class="Pixso-paragraph-5555_44120 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9032"
                class="Pixso-symbol-5615_9032"
                v-if="Progression === '60' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9033" class="Pixso-frame-5615_9033">
                    <slot name="slot_5615_9034">
                        <ProgressBarAtom
                            id="5615_9034"
                            class="Pixso-instance-5615_9034"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9035">
                        <ProgressBarAtom
                            id="5615_9035"
                            class="Pixso-instance-5615_9035"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5555_44121"
                class="Pixso-symbol-5555_44121"
                v-if="
                    Progression === '30' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44206">
                    <ProgressBar
                        id="5555_44206"
                        class="Pixso-instance-5555_44206"
                        Progression="30"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44125">
                    <p
                        id="5555_44125"
                        class="Pixso-paragraph-5555_44125 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54080"
                class="Pixso-symbol-5631_54080"
                v-if="
                    Progression === '60' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54081">
                    <ProgressBar
                        id="5631_54081"
                        class="Pixso-instance-5631_54081"
                        Progression="60"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54082">
                    <p
                        id="5631_54082"
                        class="Pixso-paragraph-5631_54082 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44126"
                class="Pixso-symbol-5555_44126"
                v-if="
                    Progression === '40' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44210">
                    <ProgressBar
                        id="5555_44210"
                        class="Pixso-instance-5555_44210"
                        Progression="40"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44130">
                    <p
                        id="5555_44130"
                        class="Pixso-paragraph-5555_44130 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54083"
                class="Pixso-symbol-5631_54083"
                v-if="
                    Progression === '60' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54084">
                    <ProgressBar
                        id="5631_54084"
                        class="Pixso-instance-5631_54084"
                        Progression="60"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54085">
                    <p
                        id="5631_54085"
                        class="Pixso-paragraph-5631_54085 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44131"
                class="Pixso-symbol-5555_44131"
                v-if="
                    Progression === '50' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44214">
                    <ProgressBar
                        id="5555_44214"
                        class="Pixso-instance-5555_44214"
                        Progression="50"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44135">
                    <p
                        id="5555_44135"
                        class="Pixso-paragraph-5555_44135 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9889"
                class="Pixso-symbol-1264_9889"
                v-if="Progression === '70' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9890" class="Pixso-frame-1264_9890">
                    <slot name="slot_1264_9891">
                        <ProgressBarAtom
                            id="1264_9891"
                            class="Pixso-instance-1264_9891"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9892">
                        <ProgressBarAtom
                            id="1264_9892"
                            class="Pixso-instance-1264_9892"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5555_44136"
                class="Pixso-symbol-5555_44136"
                v-if="
                    Progression === '60' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44218">
                    <ProgressBar
                        id="5555_44218"
                        class="Pixso-instance-5555_44218"
                        Progression="60"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44140">
                    <p
                        id="5555_44140"
                        class="Pixso-paragraph-5555_44140 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9041"
                class="Pixso-symbol-5615_9041"
                v-if="Progression === '70' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9042" class="Pixso-frame-5615_9042">
                    <slot name="slot_5615_9043">
                        <ProgressBarAtom
                            id="5615_9043"
                            class="Pixso-instance-5615_9043"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9044">
                        <ProgressBarAtom
                            id="5615_9044"
                            class="Pixso-instance-5615_9044"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5555_44141"
                class="Pixso-symbol-5555_44141"
                v-if="
                    Progression === '70' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44222">
                    <ProgressBar
                        id="5555_44222"
                        class="Pixso-instance-5555_44222"
                        Progression="70"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44145">
                    <p
                        id="5555_44145"
                        class="Pixso-paragraph-5555_44145 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54086"
                class="Pixso-symbol-5631_54086"
                v-if="
                    Progression === '70' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54087">
                    <ProgressBar
                        id="5631_54087"
                        class="Pixso-instance-5631_54087"
                        Progression="70"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54088">
                    <p
                        id="5631_54088"
                        class="Pixso-paragraph-5631_54088 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44146"
                class="Pixso-symbol-5555_44146"
                v-if="
                    Progression === '80' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44226">
                    <ProgressBar
                        id="5555_44226"
                        class="Pixso-instance-5555_44226"
                        Progression="80"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44150">
                    <p
                        id="5555_44150"
                        class="Pixso-paragraph-5555_44150 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54089"
                class="Pixso-symbol-5631_54089"
                v-if="
                    Progression === '70' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54090">
                    <ProgressBar
                        id="5631_54090"
                        class="Pixso-instance-5631_54090"
                        Progression="70"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54091">
                    <p
                        id="5631_54091"
                        class="Pixso-paragraph-5631_54091 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44151"
                class="Pixso-symbol-5555_44151"
                v-if="
                    Progression === '90' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44230">
                    <ProgressBar
                        id="5555_44230"
                        class="Pixso-instance-5555_44230"
                        Progression="90"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44155">
                    <p
                        id="5555_44155"
                        class="Pixso-paragraph-5555_44155 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9893"
                class="Pixso-symbol-1264_9893"
                v-if="Progression === '80' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9894" class="Pixso-frame-1264_9894">
                    <slot name="slot_1264_9895">
                        <ProgressBarAtom
                            id="1264_9895"
                            class="Pixso-instance-1264_9895"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9896">
                        <ProgressBarAtom
                            id="1264_9896"
                            class="Pixso-instance-1264_9896"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5555_44156"
                class="Pixso-symbol-5555_44156"
                v-if="
                    Progression === '100' && Size === 'sm' && Label === 'Bottom'
                "
            >
                <slot name="slot_5555_44234">
                    <ProgressBar
                        id="5555_44234"
                        class="Pixso-instance-5555_44234"
                        Progression="100"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5555_44160">
                    <p
                        id="5555_44160"
                        class="Pixso-paragraph-5555_44160 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5615_9050"
                class="Pixso-symbol-5615_9050"
                v-if="Progression === '80' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9051" class="Pixso-frame-5615_9051">
                    <slot name="slot_5615_9052">
                        <ProgressBarAtom
                            id="5615_9052"
                            class="Pixso-instance-5615_9052"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9053">
                        <ProgressBarAtom
                            id="5615_9053"
                            class="Pixso-instance-5615_9053"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54092"
                class="Pixso-symbol-5631_54092"
                v-if="
                    Progression === '80' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54093">
                    <ProgressBar
                        id="5631_54093"
                        class="Pixso-instance-5631_54093"
                        Progression="80"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54094">
                    <p
                        id="5631_54094"
                        class="Pixso-paragraph-5631_54094 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54095"
                class="Pixso-symbol-5631_54095"
                v-if="
                    Progression === '80' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54096">
                    <ProgressBar
                        id="5631_54096"
                        class="Pixso-instance-5631_54096"
                        Progression="80"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54097">
                    <p
                        id="5631_54097"
                        class="Pixso-paragraph-5631_54097 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9897"
                class="Pixso-symbol-1264_9897"
                v-if="Progression === '90' && Size === 'md' && Label === 'None'"
            >
                <div id="1264_9898" class="Pixso-frame-1264_9898">
                    <slot name="slot_1264_9899">
                        <ProgressBarAtom
                            id="1264_9899"
                            class="Pixso-instance-1264_9899"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9900">
                        <ProgressBarAtom
                            id="1264_9900"
                            class="Pixso-instance-1264_9900"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_9059"
                class="Pixso-symbol-5615_9059"
                v-if="Progression === '90' && Size === 'lg' && Label === 'None'"
            >
                <div id="5615_9060" class="Pixso-frame-5615_9060">
                    <slot name="slot_5615_9061">
                        <ProgressBarAtom
                            id="5615_9061"
                            class="Pixso-instance-5615_9061"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9062">
                        <ProgressBarAtom
                            id="5615_9062"
                            class="Pixso-instance-5615_9062"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54098"
                class="Pixso-symbol-5631_54098"
                v-if="
                    Progression === '90' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54099">
                    <ProgressBar
                        id="5631_54099"
                        class="Pixso-instance-5631_54099"
                        Progression="90"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54100">
                    <p
                        id="5631_54100"
                        class="Pixso-paragraph-5631_54100 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54101"
                class="Pixso-symbol-5631_54101"
                v-if="
                    Progression === '90' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54102">
                    <ProgressBar
                        id="5631_54102"
                        class="Pixso-instance-5631_54102"
                        Progression="90"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54103">
                    <p
                        id="5631_54103"
                        class="Pixso-paragraph-5631_54103 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="1264_9901"
                class="Pixso-symbol-1264_9901"
                v-if="
                    Progression === '100' && Size === 'md' && Label === 'None'
                "
            >
                <div id="1264_9902" class="Pixso-frame-1264_9902">
                    <slot name="slot_1264_9903">
                        <ProgressBarAtom
                            id="1264_9903"
                            class="Pixso-instance-1264_9903"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_1264_9904">
                        <ProgressBarAtom
                            id="1264_9904"
                            class="Pixso-instance-1264_9904"
                            Size="md"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5615_9068"
                class="Pixso-symbol-5615_9068"
                v-if="
                    Progression === '100' && Size === 'lg' && Label === 'None'
                "
            >
                <div id="5615_9069" class="Pixso-frame-5615_9069">
                    <slot name="slot_5615_9070">
                        <ProgressBarAtom
                            id="5615_9070"
                            class="Pixso-instance-5615_9070"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5615_9071">
                        <ProgressBarAtom
                            id="5615_9071"
                            class="Pixso-instance-5615_9071"
                            Size="lg"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54104"
                class="Pixso-symbol-5631_54104"
                v-if="
                    Progression === '100' && Size === 'md' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54105">
                    <ProgressBar
                        id="5631_54105"
                        class="Pixso-instance-5631_54105"
                        Progression="100"
                        Size="md"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54106">
                    <p
                        id="5631_54106"
                        class="Pixso-paragraph-5631_54106 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5631_54107"
                class="Pixso-symbol-5631_54107"
                v-if="
                    Progression === '100' && Size === 'lg' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54108">
                    <ProgressBar
                        id="5631_54108"
                        class="Pixso-instance-5631_54108"
                        Progression="100"
                        Size="lg"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54109">
                    <p
                        id="5631_54109"
                        class="Pixso-paragraph-5631_54109 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43974"
                class="Pixso-symbol-5555_43974"
                v-if="Progression === '0' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43975" class="Pixso-frame-5555_43975">
                    <slot name="slot_5555_43976">
                        <ProgressBarAtom
                            id="5555_43976"
                            class="Pixso-instance-5555_43976"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43977">
                        <ProgressBarAtom
                            id="5555_43977"
                            class="Pixso-instance-5555_43977"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54110"
                class="Pixso-symbol-5631_54110"
                v-if="Progression === '0' && Size === 'sm' && Label === 'Right'"
            >
                <slot name="slot_5631_54111">
                    <ProgressBar
                        id="5631_54111"
                        class="Pixso-instance-5631_54111"
                        Progression="0"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54112">
                    <p
                        id="5631_54112"
                        class="Pixso-paragraph-5631_54112 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "0%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43978"
                class="Pixso-symbol-5555_43978"
                v-if="Progression === '10' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43979" class="Pixso-frame-5555_43979">
                    <slot name="slot_5555_43980">
                        <ProgressBarAtom
                            id="5555_43980"
                            class="Pixso-instance-5555_43980"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43981">
                        <ProgressBarAtom
                            id="5555_43981"
                            class="Pixso-instance-5555_43981"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54113"
                class="Pixso-symbol-5631_54113"
                v-if="
                    Progression === '10' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54114">
                    <ProgressBar
                        id="5631_54114"
                        class="Pixso-instance-5631_54114"
                        Progression="10"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54115">
                    <p
                        id="5631_54115"
                        class="Pixso-paragraph-5631_54115 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "10%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43982"
                class="Pixso-symbol-5555_43982"
                v-if="Progression === '20' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43983" class="Pixso-frame-5555_43983">
                    <slot name="slot_5555_43984">
                        <ProgressBarAtom
                            id="5555_43984"
                            class="Pixso-instance-5555_43984"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43985">
                        <ProgressBarAtom
                            id="5555_43985"
                            class="Pixso-instance-5555_43985"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54116"
                class="Pixso-symbol-5631_54116"
                v-if="
                    Progression === '20' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54117">
                    <ProgressBar
                        id="5631_54117"
                        class="Pixso-instance-5631_54117"
                        Progression="20"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54118">
                    <p
                        id="5631_54118"
                        class="Pixso-paragraph-5631_54118 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "20%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43990"
                class="Pixso-symbol-5555_43990"
                v-if="Progression === '30' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43991" class="Pixso-frame-5555_43991">
                    <slot name="slot_5555_43992">
                        <ProgressBarAtom
                            id="5555_43992"
                            class="Pixso-instance-5555_43992"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43993">
                        <ProgressBarAtom
                            id="5555_43993"
                            class="Pixso-instance-5555_43993"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54119"
                class="Pixso-symbol-5631_54119"
                v-if="
                    Progression === '30' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54120">
                    <ProgressBar
                        id="5631_54120"
                        class="Pixso-instance-5631_54120"
                        Progression="30"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54121">
                    <p
                        id="5631_54121"
                        class="Pixso-paragraph-5631_54121 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "30%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43986"
                class="Pixso-symbol-5555_43986"
                v-if="Progression === '40' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43987" class="Pixso-frame-5555_43987">
                    <slot name="slot_5555_43988">
                        <ProgressBarAtom
                            id="5555_43988"
                            class="Pixso-instance-5555_43988"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43989">
                        <ProgressBarAtom
                            id="5555_43989"
                            class="Pixso-instance-5555_43989"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54122"
                class="Pixso-symbol-5631_54122"
                v-if="
                    Progression === '40' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54123">
                    <ProgressBar
                        id="5631_54123"
                        class="Pixso-instance-5631_54123"
                        Progression="40"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54124">
                    <p
                        id="5631_54124"
                        class="Pixso-paragraph-5631_54124 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "40%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43994"
                class="Pixso-symbol-5555_43994"
                v-if="Progression === '50' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43995" class="Pixso-frame-5555_43995">
                    <slot name="slot_5555_43996">
                        <ProgressBarAtom
                            id="5555_43996"
                            class="Pixso-instance-5555_43996"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_43997">
                        <ProgressBarAtom
                            id="5555_43997"
                            class="Pixso-instance-5555_43997"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54125"
                class="Pixso-symbol-5631_54125"
                v-if="
                    Progression === '50' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54126">
                    <ProgressBar
                        id="5631_54126"
                        class="Pixso-instance-5631_54126"
                        Progression="50"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54127">
                    <p
                        id="5631_54127"
                        class="Pixso-paragraph-5631_54127 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "50%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_43998"
                class="Pixso-symbol-5555_43998"
                v-if="Progression === '60' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_43999" class="Pixso-frame-5555_43999">
                    <slot name="slot_5555_44000">
                        <ProgressBarAtom
                            id="5555_44000"
                            class="Pixso-instance-5555_44000"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_44001">
                        <ProgressBarAtom
                            id="5555_44001"
                            class="Pixso-instance-5555_44001"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54128"
                class="Pixso-symbol-5631_54128"
                v-if="
                    Progression === '60' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54129">
                    <ProgressBar
                        id="5631_54129"
                        class="Pixso-instance-5631_54129"
                        Progression="60"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54130">
                    <p
                        id="5631_54130"
                        class="Pixso-paragraph-5631_54130 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "60%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44002"
                class="Pixso-symbol-5555_44002"
                v-if="Progression === '70' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_44003" class="Pixso-frame-5555_44003">
                    <slot name="slot_5555_44004">
                        <ProgressBarAtom
                            id="5555_44004"
                            class="Pixso-instance-5555_44004"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_44005">
                        <ProgressBarAtom
                            id="5555_44005"
                            class="Pixso-instance-5555_44005"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54131"
                class="Pixso-symbol-5631_54131"
                v-if="
                    Progression === '70' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54132">
                    <ProgressBar
                        id="5631_54132"
                        class="Pixso-instance-5631_54132"
                        Progression="70"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54133">
                    <p
                        id="5631_54133"
                        class="Pixso-paragraph-5631_54133 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "70%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44006"
                class="Pixso-symbol-5555_44006"
                v-if="Progression === '80' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_44007" class="Pixso-frame-5555_44007">
                    <slot name="slot_5555_44008">
                        <ProgressBarAtom
                            id="5555_44008"
                            class="Pixso-instance-5555_44008"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_44009">
                        <ProgressBarAtom
                            id="5555_44009"
                            class="Pixso-instance-5555_44009"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54134"
                class="Pixso-symbol-5631_54134"
                v-if="
                    Progression === '80' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54135">
                    <ProgressBar
                        id="5631_54135"
                        class="Pixso-instance-5631_54135"
                        Progression="80"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54136">
                    <p
                        id="5631_54136"
                        class="Pixso-paragraph-5631_54136 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "80%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44010"
                class="Pixso-symbol-5555_44010"
                v-if="Progression === '90' && Size === 'sm' && Label === 'None'"
            >
                <div id="5555_44011" class="Pixso-frame-5555_44011">
                    <slot name="slot_5555_44012">
                        <ProgressBarAtom
                            id="5555_44012"
                            class="Pixso-instance-5555_44012"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_44013">
                        <ProgressBarAtom
                            id="5555_44013"
                            class="Pixso-instance-5555_44013"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54137"
                class="Pixso-symbol-5631_54137"
                v-if="
                    Progression === '90' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54138">
                    <ProgressBar
                        id="5631_54138"
                        class="Pixso-instance-5631_54138"
                        Progression="90"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54139">
                    <p
                        id="5631_54139"
                        class="Pixso-paragraph-5631_54139 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "90%" }}
                    </p>
                </slot>
            </div>
            <div
                id="5555_44014"
                class="Pixso-symbol-5555_44014"
                v-if="
                    Progression === '100' && Size === 'sm' && Label === 'None'
                "
            >
                <div id="5555_44015" class="Pixso-frame-5555_44015">
                    <slot name="slot_5555_44016">
                        <ProgressBarAtom
                            id="5555_44016"
                            class="Pixso-instance-5555_44016"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                    <slot name="slot_5555_44017">
                        <ProgressBarAtom
                            id="5555_44017"
                            class="Pixso-instance-5555_44017"
                            Size="sm"
                            Style="Fill"
                        />
                    </slot>
                </div>
            </div>
            <div
                id="5631_54140"
                class="Pixso-symbol-5631_54140"
                v-if="
                    Progression === '100' && Size === 'sm' && Label === 'Right'
                "
            >
                <slot name="slot_5631_54141">
                    <ProgressBar
                        id="5631_54141"
                        class="Pixso-instance-5631_54141"
                        Progression="100"
                        Size="sm"
                        Label="None"
                    />
                </slot>
                <slot name="slot_5631_54142">
                    <p
                        id="5631_54142"
                        class="Pixso-paragraph-5631_54142 fill-gray60-83_2722-paragraph text-text-smsemibold-423_3209"
                    >
                        {{ "100%" }}
                    </p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import ProgressBarAtom from "@/components/Progressbaratom.vue";
import ProgressBar from "@/components/Progressbar.vue";
const props = defineProps({
    Progression: { type: String },
    Size: { type: String },
    Label: { type: String }
});
</script>
<style>
.Pixso-symbol-1264_9860 {
}
.Pixso-symbol-1264_9861 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9862 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9863 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9864 {
    width: 8px;
    height: 8px;
}
.Pixso-symbol-5615_8978 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_8979 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_8980 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_8981 {
    width: 12px;
    height: 12px;
}
.Pixso-symbol-1264_9971 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9972 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43888 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_8982 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_8983 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_8986 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54044 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54045 {
    width: 285px;
    height: 8px;
}
.Pixso-paragraph-5631_54046 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54047 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54048 {
    width: 283px;
    height: 12px;
}
.Pixso-paragraph-5631_54049 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9974 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9975 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43892 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_8991 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_8992 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_8995 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9865 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9866 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9867 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9868 {
    width: 44px;
    height: 8px;
}
.Pixso-symbol-5615_8987 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_8988 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_8989 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_8990 {
    width: 44px;
    height: 12px;
}
.Pixso-symbol-1264_9977 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9978 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43895 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9000 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9001 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9004 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54050 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54051 {
    width: 280px;
    height: 8px;
}
.Pixso-paragraph-5631_54052 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54053 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54054 {
    width: 278px;
    height: 12px;
}
.Pixso-paragraph-5631_54055 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9980 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9981 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43908 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9009 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9010 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9013 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9869 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9870 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9871 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9872 {
    width: 72px;
    height: 8px;
}
.Pixso-symbol-5615_8996 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_8997 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_8998 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_8999 {
    width: 72px;
    height: 12px;
}
.Pixso-symbol-1264_9983 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9984 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43911 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9018 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9019 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9022 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54056 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54057 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54058 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54059 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54060 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54061 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9986 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9987 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43914 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9027 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9028 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9031 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9877 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9878 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9879 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9880 {
    width: 102px;
    height: 8px;
}
.Pixso-symbol-5615_9005 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9006 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9007 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9008 {
    width: 102px;
    height: 12px;
}
.Pixso-symbol-1264_9989 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9990 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43917 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9036 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9037 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9040 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54062 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54063 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54064 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54065 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54066 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54067 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9992 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9993 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43920 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9045 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9046 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9049 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9873 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9874 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9875 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9876 {
    width: 128px;
    height: 8px;
}
.Pixso-symbol-5615_9014 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-symbol-1264_9995 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9996 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43923 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9054 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9055 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9058 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54068 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54069 {
    width: 276px;
    height: 8px;
}
.Pixso-paragraph-5631_54070 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54071 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54072 {
    width: 274px;
    height: 12px;
}
.Pixso-paragraph-5631_54073 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9998 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_9999 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43926 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9063 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9064 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9067 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9881 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9882 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9883 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9884 {
    width: 160px;
    height: 8px;
}
.Pixso-symbol-5615_9023 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9024 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9025 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9026 {
    width: 160px;
    height: 12px;
}
.Pixso-symbol-1264_10001 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-1264_10002 {
    width: 320px;
    height: 8px;
}
.Pixso-paragraph-5555_43929 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9072 {
    width: 320px;
    height: 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 12px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5615_9073 {
    width: 320px;
    height: 12px;
}
.Pixso-paragraph-5615_9076 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54074 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54075 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54076 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44106 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44194 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44110 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54077 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54078 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54079 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44111 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44198 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44115 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9885 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
.Pixso-symbol-5555_44116 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44202 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44120 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9032 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9033 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9034 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9035 {
    width: 211px;
    height: 12px;
}
.Pixso-symbol-5555_44121 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44206 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44125 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54080 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54081 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54082 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44126 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44210 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44130 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54083 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54084 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54085 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44131 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44214 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44135 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9889 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9890 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9891 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9892 {
    width: 239px;
    height: 8px;
}
.Pixso-symbol-5555_44136 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44218 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44140 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9041 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9042 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 1;
}
.Pixso-instance-5615_9043 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9044 {
    width: 239px;
    height: 12px;
}
.Pixso-symbol-5555_44141 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44222 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44145 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54086 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54087 {
    width: 278px;
    height: 8px;
}
.Pixso-paragraph-5631_54088 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44146 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44226 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44150 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5631_54089 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54090 {
    width: 276px;
    height: 12px;
}
.Pixso-paragraph-5631_54091 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44151 {
    width: 320px;
    height: 32px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44230 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44155 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-1264_9893 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9894 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9895 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9896 {
    width: 267px;
    height: 8px;
}
.Pixso-symbol-5555_44156 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 8px;
    justify-content: center;
    align-items: flex-start;
}
.Pixso-instance-5555_44234 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5555_44160 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 0;
}
.Pixso-symbol-5615_9050 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9051 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9052 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9053 {
    width: 267px;
    height: 12px;
}
.Pixso-symbol-5631_54092 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54093 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54094 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54095 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54096 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54097 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9897 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9898 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9899 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9900 {
    width: 294px;
    height: 8px;
}
.Pixso-symbol-5615_9059 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9060 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9061 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9062 {
    width: 294px;
    height: 12px;
}
.Pixso-symbol-5631_54098 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54099 {
    width: 277px;
    height: 8px;
}
.Pixso-paragraph-5631_54100 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54101 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54102 {
    width: 275px;
    height: 12px;
}
.Pixso-paragraph-5631_54103 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-1264_9901 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-1264_9902 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-1264_9903 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-1264_9904 {
    width: 320px;
    height: 8px;
}
.Pixso-symbol-5615_9068 {
    width: 320px;
    height: 12px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5615_9069 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5615_9070 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5615_9071 {
    width: 320px;
    height: 12px;
}
.Pixso-symbol-5631_54104 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
}
.Pixso-instance-5631_54105 {
    width: 270px;
    height: 8px;
}
.Pixso-paragraph-5631_54106 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5631_54107 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 12px;
    align-items: center;
}
.Pixso-instance-5631_54108 {
    width: 268px;
    height: 12px;
}
.Pixso-paragraph-5631_54109 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43974 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43975 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43976 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43977 {
    width: 8px;
    height: 4px;
}
.Pixso-symbol-5631_54110 {
    width: 353px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54111 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54112 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43978 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43979 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43980 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43981 {
    width: 44px;
    height: 4px;
}
.Pixso-symbol-5631_54113 {
    width: 358px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54114 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54115 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43982 {
    width: 320px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43983 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43984 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43985 {
    width: 72px;
    height: 4px;
}
.Pixso-symbol-5631_54116 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54117 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54118 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43990 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43991 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43992 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43993 {
    width: 102px;
    height: 4px;
}
.Pixso-symbol-5631_54119 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54120 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54121 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43986 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43987 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43988 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43989 {
    width: 128px;
    height: 4px;
}
.Pixso-symbol-5631_54122 {
    width: 362px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54123 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54124 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43994 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43995 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_43996 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_43997 {
    width: 160px;
    height: 4px;
}
.Pixso-symbol-5631_54125 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54126 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54127 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_43998 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_43999 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_44000 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_44001 {
    width: 211px;
    height: 4px;
}
.Pixso-symbol-5631_54128 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54129 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54130 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44002 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_44003 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_44004 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_44005 {
    width: 239px;
    height: 4px;
}
.Pixso-symbol-5631_54131 {
    width: 360px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54132 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54133 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44006 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_44007 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_44008 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_44009 {
    width: 267px;
    height: 4px;
}
.Pixso-symbol-5631_54134 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54135 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54136 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44010 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_44011 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_44012 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_44013 {
    width: 294px;
    height: 4px;
}
.Pixso-symbol-5631_54137 {
    width: 361px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54138 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54139 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}
.Pixso-symbol-5555_44014 {
    width: 320px;
    height: 4px;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-frame-5555_44015 {
    width: 100%;
    height: 4px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5555_44016 {
    width: 320px;
    height: 4px;
}
.Pixso-instance-5555_44017 {
    width: 320px;
    height: 4px;
}
.Pixso-symbol-5631_54140 {
    width: 368px;
    height: auto;
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
.Pixso-instance-5631_54141 {
    width: 320px;
    height: 4px;
}
.Pixso-paragraph-5631_54142 {
    text-align: right;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;
    height: auto;
    position: relative;
    flex-shrink: 0;
    white-space: pre;
    flex-grow: 0;
}

.Pixso-instance-1264_9863 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9864 .Pixso-symbol-1264_9823 {
    width: 8px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_8980 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_8981 .Pixso-symbol-1264_9819 {
    width: 12px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9972 .Pixso-symbol-1264_9861 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_8983 .Pixso-symbol-5615_8978 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54045 .Pixso-symbol-1264_9861 {
    width: 285px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54045 .Pixso-frame-1264_9862 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54045 .Pixso-instance-1264_9863 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54045 .Pixso-instance-1264_9864 {
    width: 8px;
    height: 8px;
}
.Pixso-instance-5631_54048 .Pixso-symbol-5615_8978 {
    width: 283px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54048 .Pixso-frame-5615_8979 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54048 .Pixso-instance-5615_8980 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54048 .Pixso-instance-5615_8981 {
    width: 12px;
    height: 12px;
}
.Pixso-instance-1264_9975 .Pixso-symbol-1264_9865 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9867 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9868 .Pixso-symbol-1264_9823 {
    width: 44px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_8992 .Pixso-symbol-5615_8987 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_8989 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_8990 .Pixso-symbol-1264_9819 {
    width: 44px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54051 .Pixso-symbol-1264_9865 {
    width: 280px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54051 .Pixso-frame-1264_9866 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54051 .Pixso-instance-1264_9867 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54051 .Pixso-instance-1264_9868 {
    width: 44px;
    height: 8px;
}
.Pixso-instance-5631_54054 .Pixso-symbol-5615_8987 {
    width: 278px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54054 .Pixso-frame-5615_8988 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54054 .Pixso-instance-5615_8989 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54054 .Pixso-instance-5615_8990 {
    width: 44px;
    height: 12px;
}
.Pixso-instance-1264_9978 .Pixso-symbol-1264_9869 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9871 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9872 .Pixso-symbol-1264_9823 {
    width: 72px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9001 .Pixso-symbol-5615_8996 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_8998 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_8999 .Pixso-symbol-1264_9819 {
    width: 72px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54057 .Pixso-symbol-1264_9869 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54057 .Pixso-frame-1264_9870 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54057 .Pixso-instance-1264_9871 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54057 .Pixso-instance-1264_9872 {
    width: 72px;
    height: 8px;
}
.Pixso-instance-5631_54060 .Pixso-symbol-5615_8996 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54060 .Pixso-frame-5615_8997 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54060 .Pixso-instance-5615_8998 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54060 .Pixso-instance-5615_8999 {
    width: 72px;
    height: 12px;
}
.Pixso-instance-1264_9981 .Pixso-symbol-1264_9877 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9879 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9880 .Pixso-symbol-1264_9823 {
    width: 102px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9010 .Pixso-symbol-5615_9005 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9007 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9008 .Pixso-symbol-1264_9819 {
    width: 102px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54063 .Pixso-symbol-1264_9877 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54063 .Pixso-frame-1264_9878 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54063 .Pixso-instance-1264_9879 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54063 .Pixso-instance-1264_9880 {
    width: 102px;
    height: 8px;
}
.Pixso-instance-5631_54066 .Pixso-symbol-5615_9005 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54066 .Pixso-frame-5615_9006 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54066 .Pixso-instance-5615_9007 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54066 .Pixso-instance-5615_9008 {
    width: 102px;
    height: 12px;
}
.Pixso-instance-1264_9984 .Pixso-symbol-1264_9873 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9875 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9876 .Pixso-symbol-1264_9823 {
    width: 128px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9019 .Pixso-symbol-5615_9014 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9016 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9017 .Pixso-symbol-1264_9819 {
    width: 128px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54069 .Pixso-symbol-1264_9873 {
    width: 276px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54069 .Pixso-frame-1264_9874 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54069 .Pixso-instance-1264_9875 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54069 .Pixso-instance-1264_9876 {
    width: 128px;
    height: 8px;
}
.Pixso-instance-5631_54072 .Pixso-symbol-5615_9014 {
    width: 274px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54072 .Pixso-frame-5615_9015 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54072 .Pixso-instance-5615_9016 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54072 .Pixso-instance-5615_9017 {
    width: 128px;
    height: 12px;
}
.Pixso-instance-1264_9987 .Pixso-symbol-1264_9881 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9883 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9884 .Pixso-symbol-1264_9823 {
    width: 160px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9028 .Pixso-symbol-5615_9023 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9025 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9026 .Pixso-symbol-1264_9819 {
    width: 160px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54075 .Pixso-symbol-1264_9881 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54075 .Pixso-frame-1264_9882 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54075 .Pixso-instance-1264_9883 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54075 .Pixso-instance-1264_9884 {
    width: 160px;
    height: 8px;
}
.Pixso-instance-5631_54078 .Pixso-symbol-5615_9023 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54078 .Pixso-frame-5615_9024 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54078 .Pixso-instance-5615_9025 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54078 .Pixso-instance-5615_9026 {
    width: 160px;
    height: 12px;
}
.Pixso-instance-1264_9990 .Pixso-symbol-1264_9885 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9887 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9888 .Pixso-symbol-1264_9823 {
    width: 211px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9037 .Pixso-symbol-5615_9032 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9034 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9035 .Pixso-symbol-1264_9819 {
    width: 211px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54081 .Pixso-symbol-1264_9885 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54081 .Pixso-frame-1264_9886 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54081 .Pixso-instance-1264_9887 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54081 .Pixso-instance-1264_9888 {
    width: 211px;
    height: 8px;
}
.Pixso-instance-5631_54084 .Pixso-symbol-5615_9032 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54084 .Pixso-frame-5615_9033 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54084 .Pixso-instance-5615_9034 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54084 .Pixso-instance-5615_9035 {
    width: 211px;
    height: 12px;
}
.Pixso-instance-1264_9993 .Pixso-symbol-1264_9889 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9891 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9892 .Pixso-symbol-1264_9823 {
    width: 239px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9046 .Pixso-symbol-5615_9041 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9043 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9044 .Pixso-symbol-1264_9819 {
    width: 239px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54087 .Pixso-symbol-1264_9889 {
    width: 278px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54087 .Pixso-frame-1264_9890 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54087 .Pixso-instance-1264_9891 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54087 .Pixso-instance-1264_9892 {
    width: 239px;
    height: 8px;
}
.Pixso-instance-5631_54090 .Pixso-symbol-5615_9041 {
    width: 276px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54090 .Pixso-frame-5615_9042 {
    width: 100%;
    height: auto;
    position: relative;
    flex-shrink: 0;
    flex-grow: 1;
}
.Pixso-instance-5631_54090 .Pixso-instance-5615_9043 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54090 .Pixso-instance-5615_9044 {
    width: 239px;
    height: 12px;
}
.Pixso-instance-1264_9996 .Pixso-symbol-1264_9893 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9895 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9896 .Pixso-symbol-1264_9823 {
    width: 267px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9055 .Pixso-symbol-5615_9050 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9052 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9053 .Pixso-symbol-1264_9819 {
    width: 267px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54093 .Pixso-symbol-1264_9893 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54093 .Pixso-frame-1264_9894 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54093 .Pixso-instance-1264_9895 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54093 .Pixso-instance-1264_9896 {
    width: 267px;
    height: 8px;
}
.Pixso-instance-5631_54096 .Pixso-symbol-5615_9050 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54096 .Pixso-frame-5615_9051 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54096 .Pixso-instance-5615_9052 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54096 .Pixso-instance-5615_9053 {
    width: 267px;
    height: 12px;
}
.Pixso-instance-1264_9999 .Pixso-symbol-1264_9897 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9899 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9900 .Pixso-symbol-1264_9823 {
    width: 294px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9064 .Pixso-symbol-5615_9059 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9061 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9062 .Pixso-symbol-1264_9819 {
    width: 294px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54099 .Pixso-symbol-1264_9897 {
    width: 277px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54099 .Pixso-frame-1264_9898 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54099 .Pixso-instance-1264_9899 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54099 .Pixso-instance-1264_9900 {
    width: 294px;
    height: 8px;
}
.Pixso-instance-5631_54102 .Pixso-symbol-5615_9059 {
    width: 275px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54102 .Pixso-frame-5615_9060 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54102 .Pixso-instance-5615_9061 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54102 .Pixso-instance-5615_9062 {
    width: 294px;
    height: 12px;
}
.Pixso-instance-1264_10002 .Pixso-symbol-1264_9901 {
    width: 320px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-1264_9903 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-1264_9904 .Pixso-symbol-1264_9823 {
    width: 320px;
    height: 8px;
    position: absolute;
    left: 0px;
    top: 8px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9073 .Pixso-symbol-5615_9068 {
    width: 320px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5615_9070 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5615_9071 .Pixso-symbol-1264_9819 {
    width: 320px;
    height: 12px;
    position: absolute;
    left: 0px;
    top: 11.999878px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54105 .Pixso-symbol-1264_9901 {
    width: 270px;
    height: 8px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54105 .Pixso-frame-1264_9902 {
    width: 100%;
    height: 8px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54105 .Pixso-instance-1264_9903 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54105 .Pixso-instance-1264_9904 {
    width: 320px;
    height: 8px;
}
.Pixso-instance-5631_54108 .Pixso-symbol-5615_9068 {
    width: 268px;
    height: 12px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5631_54108 .Pixso-frame-5615_9069 {
    width: 100%;
    height: 12px;
    position: relative;
    flex-shrink: 0;
}
.Pixso-instance-5631_54108 .Pixso-instance-5615_9070 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5631_54108 .Pixso-instance-5615_9071 {
    width: 320px;
    height: 12px;
}
.Pixso-instance-5555_44194 .Pixso-symbol-5555_43974 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43976 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43977 .Pixso-symbol-1264_9827 {
    width: 8px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54111 .Pixso-symbol-5555_43974 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44198 .Pixso-symbol-5555_43978 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43980 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43981 .Pixso-symbol-1264_9827 {
    width: 44px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54114 .Pixso-symbol-5555_43978 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44202 .Pixso-symbol-5555_43982 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43984 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43985 .Pixso-symbol-1264_9827 {
    width: 72px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54117 .Pixso-symbol-5555_43982 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44206 .Pixso-symbol-5555_43990 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43992 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43993 .Pixso-symbol-1264_9827 {
    width: 102px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54120 .Pixso-symbol-5555_43990 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44210 .Pixso-symbol-5555_43986 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43988 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43989 .Pixso-symbol-1264_9827 {
    width: 128px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54123 .Pixso-symbol-5555_43986 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44214 .Pixso-symbol-5555_43994 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_43996 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_43997 .Pixso-symbol-1264_9827 {
    width: 160px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54126 .Pixso-symbol-5555_43994 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44218 .Pixso-symbol-5555_43998 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44000 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_44001 .Pixso-symbol-1264_9827 {
    width: 211px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54129 .Pixso-symbol-5555_43998 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44222 .Pixso-symbol-5555_44002 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44004 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_44005 .Pixso-symbol-1264_9827 {
    width: 239px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54132 .Pixso-symbol-5555_44002 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44226 .Pixso-symbol-5555_44006 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44008 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_44009 .Pixso-symbol-1264_9827 {
    width: 267px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54135 .Pixso-symbol-5555_44006 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44230 .Pixso-symbol-5555_44010 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44012 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_44013 .Pixso-symbol-1264_9827 {
    width: 294px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54138 .Pixso-symbol-5555_44010 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44234 .Pixso-symbol-5555_44014 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
.Pixso-instance-5555_44016 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5555_44017 .Pixso-symbol-1264_9827 {
    width: 320px;
    height: 4px;
    position: absolute;
    left: 0px;
    top: 4px;
    border-radius: 1234px 1234px 1234px 1234px;
}
.Pixso-instance-5631_54141 .Pixso-symbol-5555_44014 {
    width: 320px;
    height: 4px;
    position: relative;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    border-radius: 8px 8px 8px 8px;
    background-color: transparent;
}
</style>
