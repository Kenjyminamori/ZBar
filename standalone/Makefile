
#SDK_DIR = /home/romeo/devel/humax-sdk
#SYSROOT ?=../sysroot-${platform}
OUT_DIR ?=out


MKDIR = mkdir -p ${OUT_DIR}

$(shell ${MKDIR})

.PHONY: clean install all image_scanner
	
all: image_scanner

CC_FLAGS += -I. -I.. -I../include -I../zbar

#phony targets
image_scanner: ${OUT_DIR}/image_scanner
	
%.o: %.c
	${CC} \
 	${CC_FLAGS} $< -o $@ \
 	-g \
 	-c

${OUT_DIR}/%.o: %.c
	${CC} \
 	${CC_FLAGS} $< -o $@ \
 	-g \
 	-c
 	
${OUT_DIR}/%.oxx: %.cpp
	${CXX} \
 	${CXX_FLAGS} $< -o $@ \
 	-g \
 	-c 

${OUT_DIR}/image_scanner: \
	image_scanner.o \
	../zbar/img_scanner.o   \
	../zbar/image.o \
	../zbar/symbol.o \
	../zbar/scanner.o \
	../zbar/decoder.o \
	../zbar/error.o \
	../zbar/refcnt.o \
	../zbar/decoder/ean.o \
	../zbar/decoder/code128.o \
	../zbar/decoder/qr_finder.o \
	../zbar/qrcode/qrdec.o \
	../zbar/qrcode/util.o \
	../zbar/qrcode/isaac.o \
	../zbar/qrcode/bch15_5.o \
	../zbar/qrcode/rs.o \
	../zbar/qrcode/qrdectxt.o \
	../zbar/qrcode/binarize.o
	 
	${CC} \
		-o $@ $^ \
		${CC_FLAGS} \
		-g

	

clean:
	rm -fr ${OUT_DIR}
	find .. -type f -name '*.o' -delete
	find .. -type f -name '*.lo' -delete
	find .. -type f -name '*.la' -delete
	${MKDIR}
	
distclean:
	rm -fr ${OUT_DIR}
	
install: all
	cp -f ${OUT_DIR}/* ~/nfs/temp
