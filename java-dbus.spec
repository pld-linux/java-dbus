Summary:	Java implementation of D-BUS
Summary(pl.UTF-8):	Implementacja D-BUS w Javie
Name:		java-dbus
Version:	2.3.1
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Development/Languages/Java
Source0:	http://dbus.freedesktop.org/releases/dbus-java/dbus-java-%{version}.tar.gz
# Source0-md5:	c580d4fd54868c791452290244087aeb
Patch0:		%{name}-make.patch
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	docbook-to-man
BuildRequires:	java-libmatthew
BuildRequires:	jdk >= 1.5
BuildRequires:	tex4ht
Requires:	java-libmatthew
Requires:	jre >= 1.5
Obsoletes:	java-libdbus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java implementation of D-BUS.

%description -l pl.UTF-8
Implementacja D-BUS w Javie.

%prep
%setup -q -n dbus-java-%{version}
%patch0 -p1

%build
%{__make}

%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README changelog
# javadoc
%doc doc/api
%attr(755,root,root) %{_bindir}/CreateInterface
%attr(755,root,root) %{_bindir}/DBusCall
%attr(755,root,root) %{_bindir}/DBusDaemon
%attr(755,root,root) %{_bindir}/DBusViewer
%attr(755,root,root) %{_bindir}/ListDBus
%{_javadir}/dbus*.jar
%{_mandir}/man1/CreateInterface.1*
%{_mandir}/man1/DBusCall.1*
%{_mandir}/man1/DBusDaemon.1*
%{_mandir}/man1/DBusViewer.1*
%{_mandir}/man1/ListDBus.1*
