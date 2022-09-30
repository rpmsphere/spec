Name:           shoes
Version:        3.3.7
Release:        1
BuildRequires:  gcc, ruby-devel, rubygems, rubygem-rake, rubypick
BuildRequires:  cairo-devel, pango-devel, gtk2-devel, libcurl-devel, libjpeg-devel, giflib-devel, portaudio-devel, sqlite-devel
BuildRequires:  xdg-utils, makeself
URL:            http://shoesrb.com/
Source0:        %{name}3-master.zip
Summary:        The best little GUI toolkit for Ruby
License:        MIT
Group:          Development/Languages/Ruby

%description
Shoes is a GUI Toolkit originally developed by the legendary _why.
Shoes is the best little DSL for cross-platform GUI programming there is.
It feels like real Ruby, rather than just another C++ library wrapper.
If Gtk or wxWidgets is Rails, Shoes is Sinatra.

%prep
%setup -q -n shoes3-master
#sed -i -e 's|-ljpeg|-ljpeg -lm -lruby|' -e 's|ruby-2\.1\.pc|ruby.pc|' make/*/env.rb
#sed -i -e 's|DGifOpenFileName(filename)|DGifOpenFileName(filename,NULL)|' -e 's|DGifCloseFile(gif)|DGifCloseFile(gif,NULL)|' shoes/image.c
#sed -i -e 's|lib/pkgconfig|%{_lib}/pkgconfig|' -e 's|ruby-#{rv}.pc|ruby.pc|' make/linux/env.rb

%build
rake build

%install
rake install
mkdir -p %{buildroot}%{_bindir}
mv $HOME/.shoes/federales/lib %{buildroot}%{_libdir}
install -Dm755 $HOME/.shoes/federales/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 $HOME/.shoes/federales/static/app-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
sed -i -e 's|$HOME/.shoes/federales/||' -e 's|static/app-icon|%{name}|' dist/Shoes.desktop
install -Dm644 dist/Shoes.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/ruby
%{_libdir}/%{name}
%{_libdir}/%{name}.rb
%{_libdir}/exerb
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3.7
- Rebuilt for Fedora
