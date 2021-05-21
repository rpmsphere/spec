Name:		etoys-langpack-chinese
Version:	5.0.2408
Release:	1
Summary:	Chinese language pack for eToys
License:	Apache License
Group:		User Interface/Desktops
Source0:	etoys-langpack-zh_TW.zip
Source1:	http://etoys.squeak.org/svn/trunk/Etoys/fonts/FontSimplifiedChineseEnvironment.sar
BuildArch:	noarch
BuildRequires:	gettext
Requires:	etoys

%description
Provides additional Chinese translations and fonts for eToys.

%prep
%setup -q -c

%build
for i in *.po ; do
msgfmt $i -o `basename $i .po`.mo
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/etoys/locale/zh_TW/LC_MESSAGES
cp *.mo %{buildroot}%{_datadir}/etoys/locale/zh_TW/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/etoys/fonts
cp %{SOURCE1} %{buildroot}%{_datadir}/etoys/fonts

%clean
rm -rf %{buildroot}

%files
%{_datadir}/etoys/locale/zh_TW/LC_MESSAGES
%{_datadir}/etoys/fonts/*.sar

%changelog
* Tue Feb 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.2408
- Rebuilt for Fedora
