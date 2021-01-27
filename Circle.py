from PIL import Image
import sys


class CircleDraw:

    def Circle(self, IMAGE, X_CENTER, Y_CENTER, RADIUS, COLOR = (0,0,0), BOLD = 0):

        self.IMAGE       = IMAGE     # Resim dosyası
        self.IMAGE_OPEN  = Image.open(self.IMAGE)
        self.IMAGE_PIXEL = self.IMAGE_OPEN.load()
        self.X_CENTER    = X_CENTER  # Çizilecek dairenin orta noktasındaki (x,y) X koordinatı
        self.Y_CENTER    = Y_CENTER  # Çizilecek dairenin orta noktasındaki (x,y) Y koordinatı
        self.R           = RADIUS    # Dairenin yarı çağı
        self.COLOR       = COLOR     # Çizilecek dairenin rengi
        self.BOLD        = BOLD

        self.X = self.R
        self.Y = 0
        self.P = 1 - self.R

        """
        Dairenin yarı çapı ile pixeller de gezerek 4 bölgeyi işaretliyoruz.
        İşaretlediğimiz yerler üst, alt, sağ ve soldur. Algoritma ilk olarak
        bu şekilde başlar.

        px[int(x + x_centre), int(y + y_centre)] => Orta noktamızın x eksenine
        yarı çapı ekleyerek noktamızı işaretledik. Yine y ekseni üzerinde de
        işaretlememizi yaptık. Diğer buna benzer fonksiyonlar benzeri şekilde 
        4 bölgeye işaretleme yaparak RGB değerlerini değiştirir.
        
        self.IMAGE_PIXEL[KOORDİNAT_X, KOORDİNAT_Y] = RGB COLOR
        """
        if (self.R > 0):
            self.IMAGE_PIXEL[int(self.X + self.X_CENTER),  int(self.Y + self.Y_CENTER)]    = self.COLOR
            self.IMAGE_PIXEL[int(-self.X + self.X_CENTER), int(-self.Y + self.Y_CENTER)]   = self.COLOR
            self.IMAGE_PIXEL[int(self.Y + self.X_CENTER + self.BOLD),  int(self.X + self.Y_CENTER)]    = self.COLOR
            self.IMAGE_PIXEL[int(-self.Y + self.X_CENTER), int(-self.X + self.Y_CENTER)]   = self.COLOR


        while self.X > self.Y:

            self.Y += 1

            if self.P <= 0:
                self.P = self.P + (2 * self.Y) + 1

            else:
                self.X -= 1
                self.P = self.P + (2 * self.Y) - (2 * self.X) + 1

            if (self.X < self.Y):
                # Diare çizildikten sonra programı durduruyor.
                break


            """
            Dairenin sağ ve sol köşelerini çizer.
            """
            self.IMAGE_PIXEL[
                int(self.X + self.X_CENTER),
                int(self.Y + self.Y_CENTER)
            ]   = self.COLOR

            self.IMAGE_PIXEL[
                int(-self.X + self.X_CENTER),
                int(self.Y + self.Y_CENTER)
            ]  = self.COLOR

            self.IMAGE_PIXEL[
                int(self.X + self.X_CENTER),
                int(-self.Y + self.Y_CENTER)
            ]  = self.COLOR

            self.IMAGE_PIXEL[
                int(-self.X + self.X_CENTER),
                int(-self.Y + self.Y_CENTER)
            ] = self.COLOR



            if (self.X != self.Y):

                """
                Dairenin üst ve alt köşelerini çizer.
                """
                self.IMAGE_PIXEL[
                    int(self.Y + self.X_CENTER),
                    int(self.X + self.Y_CENTER)
                ]   = self.COLOR

                self.IMAGE_PIXEL[
                    int(-self.Y + self.X_CENTER),
                    int(self.X + self.Y_CENTER)
                ]  = self.COLOR

                self.IMAGE_PIXEL[
                    int(self.Y + self.X_CENTER),
                    int(-self.X + self.Y_CENTER)
                ]  = self.COLOR

                self.IMAGE_PIXEL[
                    int(-self.Y + self.X_CENTER),
                    int(-self.X + self.Y_CENTER)
                ] = self.COLOR



    def show(self):
        self.IMAGE_OPEN.show()





