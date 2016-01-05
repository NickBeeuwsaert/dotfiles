:
COLS=$(tput cols)
while IFS= read -r line; do
    printf "%*s\n" $(((COLS + ${#line}) / 2)) "$line"
done <<EOF
                    c                                                                               
    .              cWo                                                                              
   .XWd           kMMO                                          ,xN'                                
   lMMWd        '0MMk                                   .',c0oKNMMMo                                
   XMMMK       oWMMk                                 .lNMMMMMMMMMMM:       .      .,dNk0;           
   lMMM0      xMMMx                                 .KMWWX;,,,oXMMMk     .KW.  .kNMMMMMMWo.         
   :MMMd     dMMN:                                 lXMM0;.      dMMo    .0MK .XWMMXX0NMMMMWc        
   cMMMx :O,KMMk.                                 dMMMX.        ,MMd   .0MMK.xMMO'   .OMMMMMl       
   .KMMd cMMMN:                                  KKMM0          :MMO    oMMMMMM0       c0kMMN.      
   'KMMk:NMMN.                                  .WMMMW;          XMN.  .WMMMMMN.         .MMMl      
    kMMWNMMMW'                                   kMMMMo         .WMM,  cMMMMMKO           0MMX.     
    lMMMMWxKMx                    .kOkO00c       .NMMMMc        .XMMN. lMMMMM;            .NMM;     
    ;MMMX, .OMK                   ,MMMMMMMXc     .NWMMMNo;,.';cONWMMN. cMMMMX.             OMMNK;   
   kWMMK    dMM0.                 'XWMMWKXXMk.    .,MMMMMMMMMMMMMMMMM; lMMMN.              .XMMXc   
 ,xMMMMO    c0MM0                 ,kWW0,..'WMW,     ..odOXMMNdook0NMN. ;MMMW;               oMMK    
cK0WWMMX     kMMM:               cNMMK     :NMW'        cNMK.   .;NMM' :MMMK.               oMMMc   
.,  'NMM'    'XMMW.             dMMXd;      KMMo       ;MMMd     0MM0. :MMMW'               .WMMN   
     OMM;     ,KMMO;           dMMO.        xMMN.      0MMMl    .NMMMc ;WMMW.               .NMMK   
     dMM;      ,MMMX:          dMMl         ,WMM.     kMMMN.     OMMM,  KMMM'                OMMM,  
     oMN.       dMMMK         .KMMd          :WX     OMMMK'      :NMMX..MMMM'                0MMM:  
     dMX        :NMMM,        lMMK,          :WW.   :MMMX,        kXWW'.KMMW.                xMMMl  
     xMM;        lMMMK.       :MMMc          'MM;   OMMMc        .K.XMd c0MW'                :MMMx  
     .NMo        .XMMM;       .NMMMx.       ;xMM,  'MMM0          ,oMN. l'K;                 .NMM0  
     :MMd         oMMMNl       KMMMN.     .xWMWO  .0MMM.           ;N0                        :MMX  
     ,MM:          xMMMd      .NMMMMx.   ,OMMMc   0MMkl             ::                         lNX  
      XM;           0MMK.      xWMMMMKl0WMMMM0   :MMM:                                          cMd 
      XM'           .OMMX:      .:NMMMMMMMMMX.   lMMx.                                          .Kl 
      KNx            ;MMMM:       ..0WWMWNKl.    cMo                                            ;;  
                      NXKWK            .          :.                                                
                      ;c lo                                                                         
                          .                                                                         
EOF
