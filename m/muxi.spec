Name:           muxi
Summary:        Personal TV recorder
URL:            http://muxi.sourceforge.net
License:        GPL
Group:          Productivity/Multimedia
Version:        0.8.0
Release:        1
Source0:        http://sourceforge.net/projects/muxi/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  libX11-devel, libXext-devel, mysql-devel, libxml2-devel, libjpeg-devel
BuildRequires:  xine-lib-devel
Requires:	mysql-server
Requires:	w_scan

%description
Muxi is a tv application and personal video recorder for DVB-T. It includes
an electronic programme guide, live stream recording and time shifting.

%prep
%setup -q
sed -i 's/-ljpeg/-ljpeg -lpthread/' src/Makefile.am
#sed -i 's|mmx_80w,|mmx_80w,|' src/yuv_asm.c

%build
./autogen.sh
%configure
sed -i 's|-Wall|-Wall -fPIC -DPIC|' `find . -name Makefile`
make CFLAGS+="-Wno-format-security" CFLAGS+="-fPIC -DPIC"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

install -D -m 644 tools/muxi.sql $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/muxi.sql
install -D -m 644 tools/dbchanges.sql $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/dbchanges.sql
install -D -m 644 tools/dvbs_channels_conf_2_db.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/dvbs_channels_conf_2_db.pl
install -D -m 644 tools/dvbt_channels_conf_2_db.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/dvbt_channels_conf_2_db.pl
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%_datadir/applications/%{name}.desktop
install -D -m 644 graphics/application_icon.png $RPM_BUILD_ROOT%_datadir/pixmaps/%{name}.png

%post
service mysqld start
mysqladmin -u root create muxi
mysql -u root muxi < %{_datadir}/%{name}/tools/muxi.sql
mysql -u root muxi -f < %{_datadir}/%{name}/tools/dbchanges.sql
perl %{_datadir}/%{name}/tools/dvbt_channels_conf_2_db.pl %{_datadir}/%{name}/tools/channels.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README GPL QUOTE
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}*
%{_datadir}/libxine1/fonts/arialn-*.xinefont.gz

%changelog
* Mon Jan 27 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuild for Fedora
