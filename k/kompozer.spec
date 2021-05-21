# draft by Ismael Olea <ismael@olea.org> for Fedora 10

%define cairo_version 0.5

%define minimum_build_nspr_version 4.7.2
%define minimum_build_nss_version 3.12


Name:           kompozer
Version:        0.8a4
Release:        1.zh_TW
Summary:        Web Authoring System

Group:          Applications/Publishing
License:        GPLv2+ or LGPLv2+ or MPLv1.1
URL:            http://www.kompozer.net/
Source0:        %{name}-%{version}-src.tar.bz2
Source1:        kompozer-debian-manpage
Source2:	zh-TW.zip

BuildRequires:  gcc-c++ zip
# sacado de http://cvs.fedoraproject.org/viewvc/devel/seamonkey/seamonkey.spec?revision=1.51&view=markup : 
BuildRequires:  nspr-devel >= %{minimum_build_nspr_version}
BuildRequires:  nss-devel >= %{minimum_build_nss_version}
BuildRequires:  cairo-devel >= %{cairo_version}
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libIDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  krb5-devel
BuildRequires:  pango-devel
BuildRequires:  freetype-devel >= 2.1.9
BuildRequires:  glib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  fileutils
BuildRequires:  perl
Requires:       mozilla-filesystem
Provides:       nvu = 1
Obsoletes:      nvu < 1

%description
A complete Web authoring system for Linux Desktop users, similar to
Microsoft Windows programs like FrontPage and Dreamweaver.

KompoZer is an unofficial branch of Nvu, previously developed by
Linspire Inc.

It makes managing a Web site a snap. Now anyone can create Web pages
and manage a Web site with no technical expertise or HTML knowledge.

Features

* WYSIWYG editing of pages, making Web creation as easy as typing a
   letter with your word processor.

* Integrated file management via FTP.  Simply log in to your Web
   site and navigate through your files, editing Web pages on the
   fly, directly from your site.

* Reliable HTML code creation that works with today's most popular
   browsers.

* Jump between WYSIWYG editing mode and HTML using tabs.

* Tabbed editing to make working on multiple pages a snap.

* Powerful support for frames, forms, tables, and templates.


%prep
%setup -q -c %{name}-%{version}
sed -i 's|-Wall|-fpermissive|' mozilla/configure*

%build
cd mozilla/
cp composer/config/mozconfig.fedora .mozconfig
#echo "mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-kompozer" >> .mozconfig
# this is for x64 and x32 compatibility when installing: 
# echo "mk_add_options \"CONFIGURE_ARGS= --libdir %{_libdir}\"" >> .mozconfig
echo "ac_add_options --libdir %{_libdir}" >> .mozconfig
echo "ac_add_options --with-default-mozilla-five-home=%{_libdir}/kompozer" >> .mozconfig

make -f client.mk build_all


%install
rm -rf $RPM_BUILD_ROOT

pushd obj-kompozer/xpfe/components && %__make ; popd
pushd obj-kompozer && %__make install DESTDIR=$RPM_BUILD_ROOT ;popd

# Remove internal myspell directory and myspell dicts.
# dh_install symlinks it to /usr/share/myspell where all myspell-* dicts place their stuff
rm -rf $RPM_BUILD_ROOT/%{_libdir}/kompozer/components/myspell
# Remove exec bit from .js files to prevent lintian warnings.
chmod -x $RPM_BUILD_ROOT/%{_libdir}/kompozer/components/*.js

rm -rf $RPM_BUILD_ROOT/usr/include/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/idl/

#Menu entry
install -d -m755 %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=KompoZer
Name[zh_TW]=網頁編輯者
GenericName=Web Authoring System
Comment=Create Web Pages
Comment[es]=Crea páginas web
Comment[it]=Creare pagine Web
Comment[zh_TW]=Kompozer 網頁製作系統
Categories=Development;WebDevelopment;
TryExec=%{name}
Exec=%{name} %u
Icon=/usr/lib/kompozer/icons/mozicon50.xpm
Terminal=false
MimeType=text/html;text/xml;text/css;text/x-javascript;text/javascript;application/x-php;text/x-php;application/xhtml+xml;
Type=Application
EOF

# manpage:
install -d -m755 %{buildroot}%{_mandir}/man1/
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

# spellchecker support:
#install -d -m755 %{buildroot}%{_libdir}/kompozer
install -d -m755 %{buildroot}%{_datadir}/myspell/
rm -rf %{buildroot}%{_libdir}/kompozer/dictionaries/
cd %{buildroot}%{_libdir}/kompozer
#ln -s ../../share/myspell dictionaries
ln -s %{_datadir}/myspell %{buildroot}%{_libdir}/kompozer/dictionaries

# cleaning non used devel and debug files
rm %{buildroot}%{_bindir}/kompozer-config
rm -rf %{buildroot}%{_libdir}/pkgconfig/
rm -rf %{buildroot}%{_libdir}/debug/

# replace en-US.jar with zh-TW.zip
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/kompozer/chrome/en-US.jar

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc mozilla/LEGAL mozilla/LICENSE mozilla/README.txt
%{_bindir}/kompozer
%{_libdir}/kompozer
%{_mandir}/man1/kompozer.1.gz
%{_datadir}/myspell
%{_datadir}/applications/kompozer.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8a4
- Rebuilt for Fedora
* Wed May 13 2009 Ismael Olea <ismael@olea.org> 0.8a4-1
- update to 0.8a4
* Tue May 12 2009 Ismael Olea <ismael@olea.org> 0.8a3-3
- fixing paths to build in x64
* Thu May 7 2009 Ismael Olea <ismael@olea.org> 0.8a3-2
- man page from debian, icon on desktop file, using hunspell dicts
* Thu May 7 2009 Ismael Olea <ismael@olea.org> 0.8a3-1
- first version
