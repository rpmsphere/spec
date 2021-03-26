Name:		toilet
Version:	0.3
Release:	14.3
Summary:	Powerful figlet replacement
License:	WTFPL
Group:		Text tools
URL:		http://caca.zoy.org/wiki/toilet
Source:		http://caca.zoy.org/raw-attachment/wiki/toilet/%{name}-%{version}.tar.gz
BuildRequires:	libcaca-devel zlib-devel
BuildRequires: automake

%description
TOIlet is in its very early development phase. It uses the powerful libcucul
library to achieve various text-based effects. TOIlet implements or plans to
implement the following features:
 * The ability to load FIGlet fonts
 * Support for Unicode input and output
 * Support for colour output
 * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to load
FIGlet fonts and perform horizontal smushing.

%prep
%setup -q
sed -i 's|11 10|16 15 14 13 12 11 10|' bootstrap

%build
./bootstrap
%configure
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 

%files
%_bindir/toilet
%_datadir/figlet
%_mandir/man1/toilet.*

%changelog
* Wed Jul 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Wed Jul 11 2012 pterjan <pterjan> 0.3-1.mga3
+ Revision: 269354
- Update to 0.3
- Update URLs
* Tue Feb 01 2011 pterjan <pterjan> 0.2-2.mga2
+ Revision: 45919
- imported package toilet
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 615233
- the mass rebuild of 2010.1 packages
* Sun Feb 14 2010 Pascal Terjan <pterjan@mandriva.org> 0.2-1mdv2010.1
+ Revision: 505675
- 0.2
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2010.0
+ Revision: 445495
- rebuild
* Fri Nov 14 2008 Pascal Terjan <pterjan@mandriva.org> 0.1-4mdv2009.1
+ Revision: 303147
- Fix build with as-needed
- Add upstream patch fixing build with --as-needed
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
* Wed Mar 26 2008 Pascal Terjan <pterjan@mandriva.org> 0.1-1mdv2008.1
+ Revision: 190248
- import toilet
