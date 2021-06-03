IDIR = .
CC ?= gcc
CFLAGS += -I$(IDIR)

ODIR = .

LIBS = -lm $(LDFLAGS)

.PHONY: all
all: roots_v1

$(ODIR)/%.o: %.c
	$(CC) -c $(CFLAGS) $< -o $@

roots_v1: $(ODIR)/roots_v1.o
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean
clean:
	rm -f $(ODIR)/*.o *~ roots_v1 $(IDIR)/*~ 
