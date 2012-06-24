Summary:	Set of tools for creating ringtones and logos for mobile phones
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia dzwonków i logo dla telefonów komórkowych
Name:		ringtonetools
Version:	1.06
Release:	1
License:	Kohnian
Group:		Applications/Sound
Source0:	http://65.108.58.129/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	137387c00b6d461b66816c890816c580
URL:		http://nakentone.naken.cc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ringtone Tools consists of 6 tools (rtttl2nokia, imelody2nokia,
nokia_icon, bmp2nokia_icon, midi2rtttl, imelody2wav). These programs
help in the creation of ringtones and logos for Nokia mobile phones.
For more information check the web page at http://nakentone.naken.cc/.

%description -l pl.UTF-8
Ringtone Tools składają sie z 6 narzędzi (rtttl2nokia, imelody2nokia,
nokia_icon, bmp2nokia_icon, midi2rtttl, imelody2wav). Te programy są
pomocne przy tworzeniu dzwonków i logo dla telefonów komórkowych
Nokia. Więcej informacji znajduje się na stronie
http://nakentone.naken.cc/.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rtttl2nokia imelody2nokia nokia_icon bmp2nokia_icon midi2rtttl imelody2wav \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README samples/*
%attr(755,root,root) %{_bindir}/*
