%undefine _debugsource_packages

Summary: Port of Super Bomberman, improved for X11 
Name: xbomber
Version: 0.8
Release: 1
License: GPL
Group: X11/Games   
Source: xbomber-0.8.tar.gz

%description
Super Bomberman, playable over multiple X servers,
with various improvements.

%prep
%setup -q
sed -i '426i chdir("/usr/share/xbomber");' xbomber.c

%build
make

%install
INSTPATH=%{buildroot}%{_datadir}/xbomber
mkdir -p $INSTPATH
install -Dm755 xbomber %{buildroot}%{_bindir}/xbomber

  # install pixmaps

mkdir -p $INSTPATH/pixmaps
install -m 644 -o 0 -g 0 pixmaps/block.ppm $INSTPATH/pixmaps/block.ppm
install -m 644 -o 0 -g 0 pixmaps/block2.ppm $INSTPATH/pixmaps/block2.ppm
install -m 644 -o 0 -g 0 pixmaps/bomb.ppm $INSTPATH/pixmaps/bomb.ppm
install -m 644 -o 0 -g 0 pixmaps/bones.ppm $INSTPATH/pixmaps/bones.ppm
install -m 644 -o 0 -g 0 pixmaps/box.ppm $INSTPATH/pixmaps/box.ppm
install -m 644 -o 0 -g 0 pixmaps/checker_dirt1.ppm $INSTPATH/pixmaps/checker_dirt1.ppm
install -m 644 -o 0 -g 0 pixmaps/checker_dirt2.ppm $INSTPATH/pixmaps/checker_dirt2.ppm
install -m 644 -o 0 -g 0 pixmaps/cross_dirt.ppm $INSTPATH/pixmaps/cross_dirt.ppm
install -m 644 -o 0 -g 0 pixmaps/death.ppm $INSTPATH/pixmaps/death.ppm
install -m 644 -o 0 -g 0 pixmaps/death_eating.ppm $INSTPATH/pixmaps/death_eating.ppm
install -m 644 -o 0 -g 0 pixmaps/dirt.ppm $INSTPATH/pixmaps/dirt.ppm
install -m 644 -o 0 -g 0 pixmaps/explosion1.ppm $INSTPATH/pixmaps/explosion1.ppm
install -m 644 -o 0 -g 0 pixmaps/explosion2.ppm $INSTPATH/pixmaps/explosion2.ppm
install -m 644 -o 0 -g 0 pixmaps/invert.ppm $INSTPATH/pixmaps/invert.ppm
install -m 644 -o 0 -g 0 pixmaps/invisible.ppm $INSTPATH/pixmaps/invisible.ppm
install -m 644 -o 0 -g 0 pixmaps/kicker.ppm $INSTPATH/pixmaps/kicker.ppm
install -m 644 -o 0 -g 0 pixmaps/man_down.ppm $INSTPATH/pixmaps/man_down.ppm
install -m 644 -o 0 -g 0 pixmaps/man_left.ppm $INSTPATH/pixmaps/man_left.ppm
install -m 644 -o 0 -g 0 pixmaps/man_right.ppm $INSTPATH/pixmaps/man_right.ppm
install -m 644 -o 0 -g 0 pixmaps/man_up.ppm $INSTPATH/pixmaps/man_up.ppm
install -m 644 -o 0 -g 0 pixmaps/morebomb.ppm $INSTPATH/pixmaps/morebomb.ppm
install -m 644 -o 0 -g 0 pixmaps/morefire.ppm $INSTPATH/pixmaps/morefire.ppm
install -m 644 -o 0 -g 0 pixmaps/mushroom.ppm $INSTPATH/pixmaps/mushroom.ppm
install -m 644 -o 0 -g 0 pixmaps/nuke.ppm $INSTPATH/pixmaps/nuke.ppm
install -m 644 -o 0 -g 0 pixmaps/pusher.ppm $INSTPATH/pixmaps/pusher.ppm
install -m 644 -o 0 -g 0 pixmaps/radio_bomb.ppm $INSTPATH/pixmaps/radio_bomb.ppm
install -m 644 -o 0 -g 0 pixmaps/radioupgrade.ppm $INSTPATH/pixmaps/radioupgrade.ppm
install -m 644 -o 0 -g 0 pixmaps/shield.ppm $INSTPATH/pixmaps/shield.ppm
install -m 644 -o 0 -g 0 pixmaps/title.ppm $INSTPATH/pixmaps/title.ppm
install -m 644 -o 0 -g 0 pixmaps/tnt.ppm $INSTPATH/pixmaps/tnt.ppm
install -m 644 -o 0 -g 0 pixmaps/totalfire.ppm $INSTPATH/pixmaps/totalfire.ppm
install -m 644 -o 0 -g 0 pixmaps/warp.ppm $INSTPATH/pixmaps/warp.ppm
install -m 644 -o 0 -g 0 pixmaps/you_down.ppm $INSTPATH/pixmaps/you_down.ppm
install -m 644 -o 0 -g 0 pixmaps/you_left.ppm $INSTPATH/pixmaps/you_left.ppm
install -m 644 -o 0 -g 0 pixmaps/you_right.ppm $INSTPATH/pixmaps/you_right.ppm
install -m 644 -o 0 -g 0 pixmaps/you_up.ppm $INSTPATH/pixmaps/you_up.ppm

  # install bitmaps

mkdir -p $INSTPATH/bitmaps
install -m 644 -o 0 -g 0 bitmaps/block.xbm $INSTPATH/bitmaps/block.xbm
install -m 644 -o 0 -g 0 bitmaps/block2.xbm $INSTPATH/bitmaps/block2.xbm
install -m 644 -o 0 -g 0 bitmaps/bomb.xbm $INSTPATH/bitmaps/bomb.xbm
install -m 644 -o 0 -g 0 bitmaps/bones.xbm $INSTPATH/bitmaps/bones.xbm
install -m 644 -o 0 -g 0 bitmaps/box.xbm $INSTPATH/bitmaps/box.xbm
install -m 644 -o 0 -g 0 bitmaps/cursor-mask.xbm $INSTPATH/bitmaps/cursor-mask.xbm
install -m 644 -o 0 -g 0 bitmaps/cursor.xbm $INSTPATH/bitmaps/cursor.xbm
install -m 644 -o 0 -g 0 bitmaps/death.xbm $INSTPATH/bitmaps/death.xbm
install -m 644 -o 0 -g 0 bitmaps/death_eating.xbm $INSTPATH/bitmaps/death_eating.xbm
install -m 644 -o 0 -g 0 bitmaps/dirt.xbm $INSTPATH/bitmaps/dirt.xbm
install -m 644 -o 0 -g 0 bitmaps/explosion1.xbm $INSTPATH/bitmaps/explosion1.xbm
install -m 644 -o 0 -g 0 bitmaps/explosion2.xbm $INSTPATH/bitmaps/explosion2.xbm
install -m 644 -o 0 -g 0 bitmaps/invert.xbm $INSTPATH/bitmaps/invert.xbm
install -m 644 -o 0 -g 0 bitmaps/invisible.xbm $INSTPATH/bitmaps/invisible.xbm
install -m 644 -o 0 -g 0 bitmaps/kicker.xbm $INSTPATH/bitmaps/kicker.xbm
install -m 644 -o 0 -g 0 bitmaps/man_down.xbm $INSTPATH/bitmaps/man_down.xbm
install -m 644 -o 0 -g 0 bitmaps/man_left.xbm $INSTPATH/bitmaps/man_left.xbm
install -m 644 -o 0 -g 0 bitmaps/man_right.xbm $INSTPATH/bitmaps/man_right.xbm
install -m 644 -o 0 -g 0 bitmaps/man_up.xbm $INSTPATH/bitmaps/man_up.xbm
install -m 644 -o 0 -g 0 bitmaps/morebomb.xbm $INSTPATH/bitmaps/morebomb.xbm
install -m 644 -o 0 -g 0 bitmaps/morefire.xbm $INSTPATH/bitmaps/morefire.xbm
install -m 644 -o 0 -g 0 bitmaps/mushroom.xbm $INSTPATH/bitmaps/mushroom.xbm
install -m 644 -o 0 -g 0 bitmaps/nuke.xbm $INSTPATH/bitmaps/nuke.xbm
install -m 644 -o 0 -g 0 bitmaps/pusher.xbm $INSTPATH/bitmaps/pusher.xbm
install -m 644 -o 0 -g 0 bitmaps/radio_bomb.xbm $INSTPATH/bitmaps/radio_bomb.xbm
install -m 644 -o 0 -g 0 bitmaps/radioupgrade.xbm $INSTPATH/bitmaps/radioupgrade.xbm
install -m 644 -o 0 -g 0 bitmaps/shield.xbm $INSTPATH/bitmaps/shield.xbm
install -m 644 -o 0 -g 0 bitmaps/title.xbm $INSTPATH/bitmaps/title.xbm
install -m 644 -o 0 -g 0 bitmaps/tnt.xbm $INSTPATH/bitmaps/tnt.xbm
install -m 644 -o 0 -g 0 bitmaps/totalfire.xbm $INSTPATH/bitmaps/totalfire.xbm
install -m 644 -o 0 -g 0 bitmaps/warp.xbm $INSTPATH/bitmaps/warp.xbm

  # install the ... levels ...

mkdir -p $INSTPATH/levels
for loop in levels/*; do
	install -m 644 -o 0 -g 0 $loop $INSTPATH/$loop
done

  # install the sounds

mkdir -p $INSTPATH/sounds
mkdir -p $INSTPATH/sounds/numbers
for loop in sounds/*.au; do
	install -m 644 -o 0 -g 0 $loop $INSTPATH/$loop
done
for loop in sounds/numbers/*.au; do
	install -m 644 -o 0 -g 0 $loop $INSTPATH/$loop
done

%files
%doc GRAPHICS.txt LEVELS.txt README.txt SOUND.txt
%{_bindir}/xbomber
%{_datadir}/xbomber

%changelog
* Sun Dec 11 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Sun Apr 11 1999 rufus t firefly - 0.8
- for those who want an easier install
