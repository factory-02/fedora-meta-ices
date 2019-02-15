Name:                           meta-ices
Version:                        1.0.1
Release:                        1%{?dist}
Summary:                        META-package for install and configure IceS
License:                        GPLv3

Source10:                       ices.conf

Requires:                       ices

%description
META-package for install and configure IceS.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
%{__mkdir} -p %{buildroot}%{_sysconfdir}
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/ices.conf

%files
%config %{_sysconfdir}/ices.conf

%changelog
* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
