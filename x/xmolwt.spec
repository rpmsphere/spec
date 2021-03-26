Name: xmolwt
Version: 0.7
Release: 6.1
Summary: Molecular Weight & Elemental Analysis Calculator
License: distributable
Group: Sciences/Chemistry
URL: http://www.st.hirosaki-u.ac.jp/~rmiya/xmolwt/xmolwt-e.html
Source: http://www.st.hirosaki-u.ac.jp/~rmiya/xmolwt/%name-%version.tar.gz
BuildRequires: gtk+-devel

%description 
This program calculate formula weight and percent of each elements
for the given chemical formula.

%prep
%setup -q
sed -i "s/\`\$(GTKCONFIG) --libs\` \$(OBJS) -o \$\@/\$(OBJS) -o \$\@ \`\$(GTKCONFIG) --libs\`/g" Makefile.gtk

%build
make -f Makefile.gtk CFLAGS="-DGTK %optflags" CC="gcc -Wl,--allow-multiple-definition" GTKCONFIG=gtk-config

%install
install -Dpm755 gmolwt %buildroot%_bindir/%name
ln -s xmolwt %buildroot%_bindir/molwt

install -pm 755 -d %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/xmolwt.desktop <<EOF
[Desktop Entry]
Name=XMolWt
Comment=Molecular Weight Calculator
Categories=Applications;Education;Sciences;Chemistry;
Icon=/usr/share/doc/xmolwt/xmolwt.gif
Exec=xmolwt
Terminal=0
Type=Application
EOF

%files
%doc Readme Howtouse.jp dot.gtkrc
%doc xmolwt.html xmolwt-e.html gmolwt.gif xmolwt.gif
%_bindir/xmolwt
%_bindir/molwt
%_datadir/applications/xmolwt.desktop

%changelog
* Sat May 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuild for Fedora
* Wed Feb 26 2014 Michael Shigorin <mike@altlinux.org> 0.7-alt1
- rebuilt for Sisyphus, thanks ogion@
* Fri Feb 22 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 0.7-alt0.sdg1
- build for ALTLinux
* Fri Nov 30 2001 MIYAMOTO Ryo <rmiya@cc.hirosaki-u.ac.jp>
- revised to version 0.7, changing in count.c
* Wed Aug 22 2001 MIYAMOTO Ryo <rmiya@cc.hirosaki-u.ac.jp>
- revised to version 0.6
* Tue Mar 13 2001 KAWAMURA Masao <kawamura@mlb.co.jp>
- initial rpm release
